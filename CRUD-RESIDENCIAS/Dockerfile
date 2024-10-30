# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos y la aplicación
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Expone el puerto de Flask
EXPOSE 5000

# Comando para correr la aplicación
CMD ["python", "app.py"]