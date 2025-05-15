# Imagem base com Python
FROM python:3.9-slim

# Instala Tesseract OCR, libGL e dependências do sistema
RUN apt-get update && \
    apt-get install -y tesseract-ocr libgl1 libglib2.0-0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta usada pela aplicação
EXPOSE 5000

# Comando para iniciar o servidor (ajuste se seu arquivo for outro)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
