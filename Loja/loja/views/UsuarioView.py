from urllib import request
# adicione o método de edição
#def edit_usuario_view(request):
#    print("edit_usuario")
#    print(request.user) 
#    usuario = get_object_or_404(Usuario, user=request.user)
#    print("edit_usuario1")
#    usuarioForm = UserUsuarioForm(instance=usuario)
#    print("edit_usuario2")
#    userForm = UserForm(instance=request.user)
#    print("edit_usuario3")
#    context = {
#    'usuarioForm': usuarioForm,
#    'userForm': userForm
#    }
#    return render(request, template_name='usuario/usuario-edit.html', context=context, status=200)
from django.shortcuts import render, redirect, get_object_or_404
from loja.models import Usuario
from loja.forms.UserUsuarioForm import UserUsuarioForm, UserForm

def list_usuario_view(request, id=None):
    usuarios = Usuario.objects.filter(perfil=2)
    context = {
    'usuarios': usuarios
    }
    return render(request, template_name='usuario/usuario.html', context=context, status=200)

def edit_usuario_view(request):
    print("edit_usuario_view")
    print(request.user)
    #usuario = get_object_or_404(Usuario, user=request.user)
    usuario = Usuario.objects.filter(user=request.user).first()
    print("edit_usuario_view1")
    usuarioForm = UserUsuarioForm(instance=usuario)
    print("edit_usuario_view2")
    userForm = UserForm(instance=request.user)
    context = {'usuarioForm': usuarioForm, 'userForm': userForm}
    return render(request, template_name='usuario/usuario-edit.html', context=context, status=200)