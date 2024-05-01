from django.urls import path
from .views import listar_noticias, eliminar_noticia

urlpatterns = [
    path('', listar_noticias, name='listar_noticias'),
    path('eliminar/<int:id>/', eliminar_noticia, name='eliminar_noticia'),
]
