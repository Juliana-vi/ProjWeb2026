from django.contrib import admin

# Register your models here.
from .models import * #imporata nossos models

class FabricanteAdmin(admin.ModelAdmin):
# Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'

class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgPromocao', 'preco', 'categoria',)
    empty_value_display = 'Vazio'


admin.site.register(Fabricante, FabricanteAdmin) #adiciona a interface do adm
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)

# link pra acessar: http://127.0.0.1:8080/admin
# código pra rodar: python manage.py runserver 127.0.0.1:8080
# ORDEM PARA RODAR O VENV: 
# cd loja
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# winget install Python.Python.3.11
# py -3.11 -m venv venv
# venv\Scripts\activate
# pip install django Django==4.2.7
# pip install pillow
