# HITO 1 - PROYECTO

1.⁠ ⁠Levantar primer proyecto en Django

- Utiliza el administrador de paquetes PIP para la instalación de los componentes Django.
- Crea la carpeta onlyflans
- Dentro de esta crea un entorno virtual y recuerda de activar
- Instala Django y Crea un project con el llamado onlyflans (recuerden usar el punto al final)
- Probar el Proyecto ejecutando runserver
- Preparar y migrar
- Crear user y password del admin
- Probar el Proyecto ejecutando runserver e ingresar como admin
- Crear una app llamada web
- En la views.py de web crear una función de respuesta http
- En la urls.py del proyecto anexar la route para la función previamente creada
- Modularizar la route creada (utilizando el include)
- Utiliza el utilitario manage.py para la creación de un nuevo proyecto Django.
- Subir el proyecto a gitHub (privado)

Adicional

- Crear app web
- Crear una route + view
- Modular la route a urls.py del project onyFlans

# Requerimientos

1.⁠ ⁠Crea un entorno virtual llamado onlyflans y una vez activado, comprueba que la versión de python usada es python 3. Realiza un “pantallazo” de la versión de python mostrada en la terminal/consola y guardalo en un archivo jpg o png dentro de la carpeta requerimiento1.

2.⁠ ⁠Instalar django 3.2.4 dentro del entorno virtual onlyflans, una vez instalado verifica que
haya sido instalado exitosamente utilizando el comando pip freeze. Realiza un
“pantallazo” de la versión de python mostrada en la terminal/consola y guardalo en un
archivo jpg o png dentro de la carpeta requerimiento2.

3.⁠ ⁠Usando django-admin genera un proyecto llamado onlyflans, una vez creado ingresa
a la carpeta del proyecto generado, aplica las migraciones y ejecuta tu servidor
utilizando los comandos correspondientes del archivo manage.py y accede a la url
disponible para tu proyecto. Una vez que puedas acceder a la web en tu navegador,
realiza un “pantallazo” de ésta y guardalo en un archivo jpg o png dentro de la carpeta
requerimiento3.

# ---------------------------------------------------

# ONLYFLANS

ONLYFLANS es una aplicación web de ventas de postres creada con Python y Django.

### Tecnologías

- Python 3
- Django 5

### Descripción

ONLYFLANS es una plataforma para vender y comprar postres caseros. Los usuarios pueden navegar por una variedad de postres, agregarlos a su carrito de compras y realizar pedidos.

### Características

- Registro e inicio de sesión de usuarios
- Navegación de postres disponibles
- Carrito de compras
- Realización de pedidos
- Gestión de pedidos por parte de los administradores

### Instalación y Configuración

#### Requisitos Previos

- Python 3.x
- Pip (gestor de paquetes de Python)
- Virtualenv (opcional, pero recomendado)

#### Pasos de Instalación

1. Clona el repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd onlyflans
   ```

2. Crea y activa un entorno virtual:

   ```bash
   virtualenv venv
   source venv/Scripts/activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno en un archivo `.env` (opcional):

   ```env
   DEBUG=True
   SECRET_KEY=your_secret_key
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. Realiza las migraciones de la base de datos:

   ```bash
   python manage.py makemigrations
   ```

   ```bash
   python manage.py migrate
   ```

6. Crea un superusuario para acceder al panel de administración:

   ```bash
   python manage.py createsuperuser
   ```

7. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

### Uso

1. Abre tu navegador web y navega a `http://localhost:8000/` para ver la página de inicio.
2. Usa el panel de administración en `http://localhost:8000/admin/` para gestionar el contenido de la aplicación.

### Rutas

- `/` - Página principal
- `/curriculum` - Página de ejemplo de plantilla

### Estructura del Proyecto

Una descripción rápida de la estructura de directorios principal:

```plaintext
onlyflans/
├── manage.py
├── onlyflans/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── web/
│   │__init__.py
│   │── admin.py
│   │── models.py
│   │── views.py
│   ├── urls.py
├── templates/
│   ├── index.html
│   ├── curriculum.html
├── static/
│   ├── css/styles.css
│   ├── js/index.js
│   ├── ...
├── ...
```

### Integrantes

- Rubén Mario Ramírez Itashiki
  - [GitHub](https://github.com/XR-Ruben/onlyflans.git)
- Jorge Rodriguez Oliva
  - [GitHub](<enlace github>)

### Contribuir

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una rama con tu nueva característica (`git checkout -b feature/nueva-caracteristica`).
3. Haz commit de tus cambios (`git commit -m 'Añadida nueva característica'`).
4. Empuja tu rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

### Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

### Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarnos a través de [email@example.com].
