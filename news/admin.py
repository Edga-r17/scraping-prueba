from django.contrib import admin

# Register your models here.
from news.models import Noticia
from rangefilter.filters import DateRangeFilter


class NoticiaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'descripcion', 
        'autor',
        'fecha_publicacion',
        'eliminado',
    )

    search_fields = ['titulo', 'fecha_publicacion' ]
    list_filter = (('fecha_publicacion', DateRangeFilter),)
    list_editable = ['eliminado']

admin.site.register(Noticia, NoticiaAdmin)
