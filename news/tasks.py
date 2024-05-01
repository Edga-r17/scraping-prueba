import requests
from bs4 import BeautifulSoup
from .models import Noticia

def scrape_noticias():
    url = 'https://elpais.com/noticias/pirata-informatico/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articulos = soup.find_all('article') 

    for articulo in articulos:
        titulo = articulo.find('h2').text.strip() if articulo.find('h2') else 'Título no disponible'
        descripcion = articulo.find('p').text.strip() if articulo.find('p') else 'Descripción no disponible'

        # Buscando el enlace del autor por clase y verificando antes de acceder a .text
        autor_link = articulo.find('a', class_='c_a_a')
        autor = autor_link.text.strip() if autor_link else 'Autor no disponible'

        # Asegurándose de que el elemento 'time' exista antes de intentar acceder a 'datetime'
        time_element = articulo.find('time')
        fecha = time_element['datetime'] if time_element else 'Fecha no disponible'



        Noticia.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            autor=autor,
            fecha_publicacion=fecha
        )
