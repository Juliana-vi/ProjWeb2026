from django.urls import path
from loja.views.FavoritoView import favoritar_view, list_favorito_view
urlpatterns = [
    path("", list_favorito_view, name='list_favorito'),
    path("<int:produto_id>", favoritar_view, name='favoritar'),
]