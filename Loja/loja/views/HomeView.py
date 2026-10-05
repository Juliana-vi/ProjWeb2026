#from django.http import HttpResponse
#def home_view(request):
#   return HttpResponse('<h1>Olá mundo!</h1>')
from django.shortcuts import render
from loja.models import Produto, Favorito
def home_view(request):
    produto = request.GET.get("produto")
    produtos = Produto.objects.all()
    if produto is not None:
        produtos = produtos.filter(Produto__contains=produto)
    # ids dos produtos favoritos do usuário logado, para marcar o botão de favoritar
    favoritos_ids = []
    if request.user.is_authenticated:
        favoritos_ids = list(Favorito.objects.filter(user=request.user).values_list('produto_id', flat=True))
    context = {
        'produtos': produtos,
        'favoritos_ids': favoritos_ids
    }
    return render(request, template_name='home/home.html', context=context, status=200)