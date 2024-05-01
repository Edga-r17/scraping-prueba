# Scraping Prueba

En este proyecto se desarrolla un proyecto prueba que realiza scraping a la [pagina](https://elpais.com/noticias/pirata-informatico/)

---
### Stack :computer:

El proyecto esta construido sobre el siguiente stack tecnológico:

- Python 3.9.0
- Django 4.2.11
- PostgresSQL

---
## Clonar Proyecto 

Pasos detallados para instalar el proyecto:

1. git clone (https://github.com/Edga-r17/scraping-prueba.git)
2. cd middle
3. pip install -r requirements.txt

---

### Instalación :tools:

Despues de clonar este proyecto en el directorio local correspondiente, se deben ejecutar los siguientes pasos:

1. Crear archivo `.env` en reaiz de proyecto con el contenido de las variables globales.
3. Crear el ambiente virtual usando [pyenv](https://github.com/pyenv/pyenv#installation)
4. Activar el `pyenv activate <nombre del ambiente creado>`
5. Correr el comando `source .env` para exportar las variables de archivo anterior.
6. Instalar las dependencias del proyecto `pip install -r requirements.txt`
7. Correr migraciones: `python manage.py migrate`
8. Correr el proyecto: `python manage.py runserver`

---

### Ejecutar Scraping

Ya una vez instalado todo lo necesario para correr el proyecto, ejecutaremos el scrping con los siguiente pasos:
1. Activar el `pyenv activate <nombre del ambiente creado>`
2. Correr el comando `source .env` para exportar las variables de archivo anterior.
3. Correr el shell: `python manage.py shell`
4. Escribir en el shell: `from news.tasks import scrape_noticias`
5. Despues escribir: `scrape_noticias()`


