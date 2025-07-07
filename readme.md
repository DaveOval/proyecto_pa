# Proyecto PA - Sistema de Reseñas de Películas

## Características

- **Autenticación de Usuarios**: Registro, inicio de sesión y gestión de perfiles
- **Gestión de Películas**: Agregar, ver y gestionar películas
- **Sistema de Reseñas**: Calificar y comentar películas (1-5 estrellas)
- **Dashboard Interactivo**: Vista principal con todas las películas
- **Seguridad**: Contraseñas encriptadas con bcrypt y JWT
- **Base de Datos**: PostgreSQL con SQLModel para ORM

## Tecnologías Utilizadas

- **Backend**: Python 3.8+
- **Framework**: Reflex
- **Base de Datos**: PostgreSQL
- **ORM**: SQLModel
- **Autenticación**: JWT + bcrypt
- **Variables de Entorno**: python-dotenv

## Requisitos Previos

- Python 3.8 o superior
- PostgreSQL instalado y configurado
- pip (gestor de paquetes de Python)
- Git

## Instalación

### 1. Clonar el Repositorio

```bash
git clone <https://github.com/DaveOval/proyecto_pa>
cd proyecto_pa
```

### 2. Crear Entorno Virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En macOS/Linux:
source venv/bin/activate
# En Windows:
venv\Scripts\activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt
```

## Configuración

### 1. Configurar Variables de Entorno

Crear un archivo `.env` en la raíz del proyecto:

```bash
# Archivo .env
LLAVE_SECRETA_JWT=tu_clave_secreta_muy_segura_aqui
APP_NAME=Proyecto PA - Sistema de Reseñas
URL_POSTGRES_URL=postgresql://usuario:contraseña@localhost:5432/nombre_base_datos
```

### 2. Configurar Base de Datos PostgreSQL

1. Crear una base de datos PostgreSQL:
```sql
CREATE DATABASE nombre_base_datos;
```

2. Configurar las credenciales en la URL de conexión del archivo `.env`

### 3. Configurar Alembic (Migraciones)

```bash
# Inicializar Alembic (si no está configurado)
alembic init alembic

# Crear migración inicial
alembic revision --autogenerate -m "Initial migration"

# Ejecutar migraciones
alembic upgrade head
```

## Ejecución

### Desarrollo Local

```bash
# Activar entorno virtual (si no está activado)
source venv/bin/activate

# Ejecutar la aplicación en modo desarrollo
reflex run
```

La aplicación estará disponible en: `http://localhost:3000`


## Estructura del Proyecto

```
proyecto_pa/
├── alembic/                    # Migraciones de base de datos
│   ├── versions/              # Archivos de migración
│   └── env.py                 # Configuración de Alembic
├── assets/                    # Archivos estáticos
├── entregables/              # Documentación y capturas
├── proyecto_pa/              # Código principal
│   ├── components/           # Componentes reutilizables
│   │   └── navbar.py         # Barra de navegación
│   ├── models/               # Modelos de base de datos
│   │   ├── usuarios.py       # Modelo de usuarios
│   │   ├── peliculas.py      # Modelo de películas
│   │   └── reviews.py        # Modelo de reseñas
│   ├── pages/                # Páginas de la aplicación
│   │   ├── dashboard.py      # Dashboard principal
│   │   ├── login.py          # Página de inicio de sesión
│   │   ├── signup.py         # Página de registro
│   │   ├── add_movie.py      # Agregar película
│   │   ├── ver_pelicula.py   # Ver detalles de película
│   │   └── info.py           # Página de información
│   ├── state/                # Estado global de la aplicación
│   │   └── app_state.py      # Estado compartido
│   ├── Auth.py               # Lógica de autenticación
│   └── proyecto_pa.py        # Archivo principal de la aplicación
├── appconfig.py              # Configuración de la aplicación
├── requirements.txt          # Dependencias de Python
├── rxconfig.py              # Configuración de Reflex
└── alembic.ini              # Configuración de Alembic
```

## Funcionalidades

### Autenticación
- **Registro de Usuarios**: Crear nuevas cuentas con validación
- **Inicio de Sesión**: Autenticación segura con JWT
- **Gestión de Perfiles**: Información del usuario y estado

### Gestión de Películas
- **Agregar Películas**: Formulario para crear nuevas películas
- **Ver Películas**: Lista de todas las películas disponibles
- **Detalles de Película**: Vista detallada con reseñas

### Sistema de Reseñas
- **Crear Reseñas**: Comentar y calificar películas (1-5 estrellas)
- **Ver Reseñas**: Mostrar todas las reseñas de una película
- **Gestión de Reseñas**: Los usuarios pueden ver sus reseñas

## Base de Datos

### Modelos Principales

#### Usuarios
- `id`: Identificador único
- `nombre`: Nombre del usuario
- `email`: Correo electrónico
- `password`: Contraseña encriptada
- `role`: Rol del usuario (user/admin)
- `status`: Estado del usuario (active/inactive)

#### Películas
- `id`: Identificador único
- `titulo`: Título de la película
- `descripcion`: Descripción de la película
- `fecha_lanzamiento`: Fecha de lanzamiento
- `creador_por_id`: ID del usuario que la creó
- `created_at`: Fecha de creación

#### Reviews
- `id`: Identificador único
- `comentario`: Comentario de la reseña
- `calificacion`: Calificación (1-5)
- `usuario_id`: ID del usuario que escribió la reseña
- `pelicula_id`: ID de la película reseñada
- `creado_en`: Fecha de creación

## 🔗 API y Rutas

### Páginas Principales
- `/`: Página de bienvenida
- `/login`: Inicio de sesión
- `/signup`: Registro de usuario
- `/dashboard`: Dashboard principal con películas
- `/add_movie`: Agregar nueva película
- `/pelicula/{id}`: Ver detalles de película
- `/info`: Información del proyecto

### Funcionalidades de Estado
- **AuthState**: Manejo de autenticación y tokens JWT
- **AppState**: Estado compartido entre componentes
- **EstadoDashboard**: Estado específico del dashboard

## Comandos Útiles

```bash
# Ejecutar en desarrollo
reflex run

# Construir para producción
reflex export

# Ejecutar migraciones
alembic upgrade head

# Crear nueva migración
alembic revision --autogenerate -m "Descripción del cambio"

# Ver estado de migraciones
alembic current
alembic history
```
