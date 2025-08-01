# Imagen base oficial de Python
FROM python:3.11

# Establecer directorio de trabajo
WORKDIR /app

# Copiar los archivos al contenedor
COPY . /app

# Instalar dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Crear carpeta para medios y estáticos
RUN mkdir -p /app/media /app/static

# Comando por defecto para correr el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
