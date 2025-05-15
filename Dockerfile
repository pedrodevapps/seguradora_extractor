# Imagem base com Python
FROM python:3.9-slim

# Instala o Tesseract OCR e dependências básicas
RUN apt-get update && \
    apt-get install -y tesseract-ocr && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta usada pela aplicação (Render usa por padrão)
EXPOSE 5000

# Comando para iniciar o servidor (ajuste se sua app tiver outro nome)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
