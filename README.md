# Chaindots


`Proyecto creado como test. se utilizó Django para la solución de los requerimientos`

# Instalación

##### 1) Clonar o descargar el proyecto del repositorio

`git clone https://github.com/ildecarz/Chaindots.git`

##### 2) Crear un entorno virtual para posteriormente instalar las librerias del proyecto

- `python3 -m venv venv` (Windows)
-  `virtualenv venv -p python3` (Linux)

##### 3) Activar el entorno virtual de nuestro proyecto

- `cd venv\Scripts\activate.bat` (Windows)
- `source venv/bin/active` (Linux)

##### 4) Instalar todas las librerias del proyecto que se encuentran en requirements.txt

- `pip install -r requirements.txt`

##### 5) Crear la base de datos con las migraciones y el superuser para iniciar sesión

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`


##### 6) Para acceder al servidor

- `python manage.py runserver`