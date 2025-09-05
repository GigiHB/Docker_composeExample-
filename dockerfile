# Usamos imagen oficial de Python
FROM python:3.11-slim

# Establecemos directorio de trabajo
WORKDIR /app

# Copiamos archivos de proyecto
COPY requirements.txt .

# Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

#Copy app
COPY app.py .


# Comando para ejecutar la app
CMD ["python", "app.py"]