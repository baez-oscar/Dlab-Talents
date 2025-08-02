# 📄 dTalent Recibos Online – Backend API

API RESTful desarrollada en **Django + Django REST Framework** para gestionar usuarios y recibos de sueldo digitales. Este backend permite autenticación, consulta filtrada de usuarios y recibos, así como la descarga de archivos PDF de los mismos.

---

##  Funcionalidades

-  Autenticación con token (`Authorization: Token <token>`)
-  Gestión de usuarios con filtrado por nacionalidad
-  Listado y filtrado de recibos (por año, mes, empleado)
-  Visualización y descarga de recibos PDF
-  Protección por permisos de acceso (`IsAuthenticated`)
-  Filtros por URL query
-  Datos de ejemplo para pruebas

---

##  Estructura del Proyecto

```
dlab-talents/
├── apps/
│   ├── authentication/    # Login y autenticación
│   ├── users/             # Modelo de usuario extendido
│   └── receipts/          # Modelo de recibos
├── config/                # Configuración global de Django
├── media/                 # Archivos PDF cargados
├── static/                # Archivos estáticos (admin u otros)
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

##  Configuración del Entorno

### 1. Variables de entorno

Crea un archivo `.env` con tus credenciales (No se ignoro el archivo .env para facilitar la ejecucion):

```env
DB_NAME=dlab_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

---

### 2. Inicialización automática del entorno

Ejecutar los siguientes comandos o directamente setup.bat (Windows CMD o PowerShell) o setup.sh(Git Bash / WSL / Linux / macOS):

```bash


docker-compose down -v
docker-compose build --no-cache
docker-compose up -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser 
docker-compose exec web python manage.py load_data


```

> Accede a la API en: `http://localhost:8000`


---

## 🔑 Autenticación

### Endpoint de login:

```
POST /auth/login/
```

#### Body (JSON):

```json
{
  "username": "admin",
  "password": "adminpass"
}
```

#### Header de autenticación para otros endpoints:

```
Authorization: Token <token>
```

---

##  Endpoints principales

###  Autenticación

| Método | Ruta           | Descripción                  |
|--------|----------------|------------------------------|
| POST   | /auth/login/   | Obtener token de login       |

---

###  Usuarios

| Método | Ruta       | Descripción                              |
|--------|------------|------------------------------------------|
| GET    | /users/    | Listado de usuarios (requiere token)     |

**Parámetros de filtro:**
- `nationality=Paraguay`

---

###  Recibos

| Método | Ruta           | Descripción                              |
|--------|----------------|------------------------------------------|
| GET    | /receipts/     | Listado de recibos (requiere token)      |
| GET    | /receipts/{id}/file | Descarga el archivo PDF del recibo     |

**Parámetros de filtro:**
- `year=2025`
- `month=7`
- `employee_number=123`

---

##  Testing

Para ejecutar los tests automáticos:

```bash
docker-compose exec web pytest
```

Los tests incluyen:
- Listado de recibos autenticado y no autenticado
- Descarga de archivos PDF
- Validación de permisos

---


