import pytesseract
import cv2
import re
from pdf2image import convert_from_path
from PIL import Image
import os
import numpy as np

# NOVO: Função para redimensionar imagem
def resize_image(img, max_width=1000):
    h, w = img.shape[:2]
    if w > max_width:
        scale = max_width / w
        img = cv2.resize(img, (int(w * scale), int(h * scale)))
    return img

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    gray = resize_image(gray)  # <- Reduz tamanho da imagem aqui
    return gray

def extract_text(image_path):
    img = preprocess_image(image_path)
    return pytesseract.image_to_string(img, lang='por')

def extract_data_from_text(text):
    data = {
        "nome": re.search(r"(?i)nome[:\s]*([A-ZÃ-Úa-zã-ú\s]+)", text),
        "cpf": re.search(r"(?i)cpf[:\s]*([\d.\-]+)", text),
        "rg": re.search(r"(?i)rg[:\s]*([\d.\-]+)", text),
        "nascimento": re.search(r"(?i)nascimento[:\s]*([\d/]+)", text),
        "sexo": re.search(r"(?i)sexo[:\s]*([MF])", text),
        "estado_civil": re.search(r"(?i)estado civil[:\s]*([A-Za-z]+)", text),
        "endereco": re.search(r"(?i)endere[cç]o[:\s]*(.+)", text),
        "cep": re.search(r"(?i)cep[:\s]*([\d\-]+)", text),
        "cidade": re.search(r"(?i)cidade[:\s]*([A-ZÃ-Úa-zã-ú\s]+)", text),
        "estado": re.search(r"(?i)estado[:\s]*([A-Z]{2})", text),
        "telefone": re.search(r"(?i)telefone[:\s]*([\d().\-\s]+)", text),
        "celular": re.search(r"(?i)celular[:\s]*([\d().\-\s]+)", text),
        "email": re.search(r"(?i)e[-]?mail[:\s]*([\w\.-]+@[\w\.-]+)", text),
        "observacoes": re.search(r"(?i)observa[cç][õo]es[:\s]*(.*)", text),
    }
    return {k: (v.group(1).strip() if v else "") for k, v in data.items()}

def extract_data_from_file(path):
    ext = os.path.splitext(path)[-1].lower()
    if ext == ".pdf":
        images = convert_from_path(path)
        temp_path = "temp_image.jpg"
        images[0].save(temp_path, 'JPEG')
        text = extract_text(temp_path)
        os.remove(temp_path)
    else:
        text = extract_text(path)
    return extract_data_from_text(text)
