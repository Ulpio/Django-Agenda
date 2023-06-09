from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User


# Create your views here.

# def index(request):
#     return redirect('/agenda')
def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username,password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('/')
        else:
            messages.error(request,"Usuário ou Senha Inválida.")
    return redirect('/')


def create_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=username, email=email, password=password)
        return HttpResponseRedirect('/success/')

    return render(request, 'create_user.html')

def submit_user(request):
    if request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
    return redirect('/')


@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request,'evento.html',dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        localizacao = request.POST.get('localizacao')
        id_evento = request.POST.get('id_evento')
        usuario = request.user
        if id_evento:
            Evento.objects.filter(id=id_evento).update(titulo=titulo,
                              data_evento=data_evento,
                              descricao=descricao,
                              localizacao=localizacao)
        else:
            Evento.objects.create(titulo=titulo,
                              data_evento=data_evento,
                              descricao=descricao,
                              localizacao=localizacao,
                              usuario=usuario)
    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request,id_evento):
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)
    if usuario == evento.usuario:
        evento.delete()
    return redirect('/')