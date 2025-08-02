#!/bin/bash

echo " 1. Apagando y limpiando contenedores anteriores..."
docker-compose down -v

echo " 2. Rebuild del proyecto desde cero..."
docker-compose build --no-cache

echo " 3. Levantando servicios..."
docker-compose up -d

echo " 4. Esperando a que la base de datos esté lista..."
sleep 10

echo " 5. Aplicando migraciones..."
docker-compose exec web python manage.py migrate

echo " 6. Creando superusuario (admin / admin123)..."
docker-compose exec web python manage.py createsuperuser --noinput || echo "Ya existe"

echo " 7. Cargando datos de prueba..."
docker-compose exec web python manage.py load_data

