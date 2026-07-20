from django.shortcuts import render, redirect
from loja.models import Categoria


def list_categoria_view(request, id=None):
    categoria = request.GET.get("categoria")
    categorias = Categoria.objects.all()

    if categoria is not None:
        categorias = categorias.filter(Categoria__contains=categoria)
    if id is not None:
        categorias = categorias.filter(id=id)

    context = {'categorias': categorias}
    return render(request, template_name='categoria/categoria.html', context=context, status=200)


def create_categoria_view(request):
    if request.method == 'POST':
        categoria = request.POST.get("Categoria")
        try:
            obj_categoria = Categoria()
            obj_categoria.Categoria = categoria
            obj_categoria.save()
            print("Categoria %s salva com sucesso" % categoria)
        except Exception as e:
            print("Erro inserindo categoria: %s" % e)
        return redirect("/categoria")
    return render(request, template_name='categoria/categoria-create.html', status=200)


def edit_categoria_view(request, id=None):
    categorias = Categoria.objects.all()
    if id is not None:
        categorias = categorias.filter(id=id)
    categoria = categorias.first()
    context = {'categoria': categoria}
    return render(request, template_name='categoria/categoria-edit.html', context=context, status=200)


def edit_categoria_postback(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        categoria = request.POST.get("Categoria")
        try:
            obj_categoria = Categoria.objects.filter(id=id).first()
            obj_categoria.Categoria = categoria
            obj_categoria.save()
            print("Categoria %s salva com sucesso" % categoria)
        except Exception as e:
            print("Erro salvando edição de categoria: %s" % e)
    return redirect("/categoria")


def delete_categoria_view(request, id=None):
    categorias = Categoria.objects.all()
    if id is not None:
        categorias = categorias.filter(id=id)
    categoria = categorias.first()
    context = {'categoria': categoria}
    return render(request, template_name='categoria/categoria-delete.html', context=context, status=200)


def delete_categoria_postback(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        categoria = request.POST.get("Categoria")
        try:
            Categoria.objects.filter(id=id).delete()
            print("Categoria %s excluida com sucesso" % categoria)
        except Exception as e:
            print("Erro excluindo categoria: %s" % e)
    return redirect("/categoria")
