from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada") #O que aparece no display admin
    list_display_links = ("id", "nome") #Links no nome "ID" e "Nome"
    search_fields = ("nome",) #Campo de Pesquisa
    list_filter = ("categoria",) #Filtros da direita
    list_editable = ("publicada",) #Poder editar no admin
    list_per_page = 10 #O máximo de conteúdo por página admin

admin.site.register(Fotografia, ListandoFotografias)
