from django.shortcuts import render, redirect, get_object_or_404
from loja.models import Fabricante
from loja.forms.FabricanteForm import FabricanteForm


def list_fabricante_view(request, id=None):
    fabricante = request.GET.get("fabricante")
    fabricantes = Fabricante.objects.all()

    if fabricante is not None:
        fabricantes = fabricantes.filter(Fabricante__contains=fabricante)
    if id is not None:
        fabricantes = fabricantes.filter(id=id)

    context = {'fabricantes': fabricantes}
    return render(request, template_name='fabricante/fabricante.html', context=context, status=200)


def create_fabricante_view(request):
    message = None
    if request.method == 'POST':
        fabricanteForm = FabricanteForm(request.POST)
        if fabricanteForm.is_valid():
            fabricanteForm.save()
            return redirect("/fabricante")
        else:
            message = {'type': 'danger', 'text': 'Dados inválidos'}
    else:
        fabricanteForm = FabricanteForm()

    context = {'fabricanteForm': fabricanteForm, 'message': message}
    return render(request, template_name='fabricante/fabricante-create.html', context=context, status=200)


def edit_fabricante_view(request, id=None):
    fabricante = get_object_or_404(Fabricante, id=id)
    message = None

    if request.method == 'POST':
        fabricanteForm = FabricanteForm(request.POST, instance=fabricante)
        if fabricanteForm.is_valid():
            fabricanteForm.save()
            message = {'type': 'success', 'text': 'Dados atualizados com sucesso'}
        else:
            message = {'type': 'danger', 'text': 'Dados inválidos'}
    else:
        fabricanteForm = FabricanteForm(instance=fabricante)

    context = {'fabricanteForm': fabricanteForm, 'message': message}
    return render(request, template_name='fabricante/fabricante-edit.html', context=context, status=200)


def delete_fabricante_view(request, id=None):
    fabricante = get_object_or_404(Fabricante, id=id)
    if request.method == 'POST':
        try:
            fabricante.delete()
            print("Fabricante excluído com sucesso")
        except Exception as e:
            print("Erro excluindo fabricante: %s" % e)
        return redirect("/fabricante")

    context = {'fabricante': fabricante}
    return render(request, template_name='fabricante/fabricante-delete.html', context=context, status=200)