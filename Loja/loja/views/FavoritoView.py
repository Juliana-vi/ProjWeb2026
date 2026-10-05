from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from loja.models import Produto, Favorito

# Função para favoritar/desfavoritar um produto, login obrigatorio
@login_required
def favoritar_view(request, produto_id=None):
    print ('favoritar_view')
    produto = get_object_or_404(Produto, pk=produto_id)
    favorito = Favorito.objects.filter(user=request.user, produto=produto).first()
    if favorito:
        # Se o produto já é favorito do usuário, retira dos favoritos
        favorito.delete()
        print ('produto desfavoritado: ' + str(produto.id))
    else:
        # Se ainda não é favorito, inclui nos favoritos
        Favorito.objects.create(user=request.user, produto=produto)
        print ('produto favoritado: ' + str(produto.id))
    return redirect('/')

# Função para listar os produtos favoritos do usuário, login obrigatorio
@login_required
def list_favorito_view(request):
    print ('list_favorito_view')
    favoritos = Favorito.objects.filter(user=request.user).select_related('produto')
    context = {
        'favoritos': favoritos
    }
    return render(request, template_name='favorito/favorito.html', context=context, status=200)