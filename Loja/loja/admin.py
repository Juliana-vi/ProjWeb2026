from django.contrib import admin

# Register your models here.
from .models import * #imporata nossos models

class FabricanteAdmin(admin.ModelAdmin):
# Cria um filtro de hierarquia com datas
    date_hierarchy = 'criado_em'


admin.site.register(Fabricante, FabricanteAdmin) #adiciona a interface do adm
admin.site.register(Categoria)
admin.site.register(Produto)

# código pra acessar: http://127.0.0.1:8080/admin
# código pra rodar: python manage.py runserver 127.0.0.1:8080