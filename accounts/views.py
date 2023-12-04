from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse

from accounts.models import Estudante, CustomUser


def user_login(request):
    if request.method == 'POST':
        nomeEstudante = request.POST.get('username')  # Suponha que o campo seja 'username'
        password = request.POST.get('password')  # Suponha que o campo seja 'password'

        user = authenticate(request, username=nomeEstudante, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Credenciais inválidas, exibe a página de login novamente ou uma mensagem de erro
            return render(request, 'pages/login.html', {'erro': 'Credenciais inválidas'})

    return render(request, 'pages/login.html')


def user_logout(request):
  auth.logout(request)
  return redirect('home')


def user_register(request):
    if request.method == 'POST':
      nomeEstudante = request.POST.get('username')
      cpf = request.POST.get('cpf')
      rua = request.POST.get('rua')
      bairro = request.POST.get('bairro')
      cidade = request.POST.get('cidade')
      cep = request.POST.get('cep')
      matriculaEstudante = request.POST.get('matricula')
      curso = request.POST.get('curso')
      email = request.POST.get('email')
      password = request.POST.get('password')
      passwordConfirm = request.POST.get('repeat-pass')

      # try:
      estudante = Estudante.objects.create(nomeEstudante=nomeEstudante, cpf=cpf, rua=rua, bairro=bairro,
                                           cidade=cidade,
                                           cep=cep, password=password, email=email,
                                           matriculaEstudante=matriculaEstudante, curso=curso)
      user = CustomUser.objects.create_user(username=nomeEstudante, email=email, password=password)
      user.estudante = estudante
      user.save()
      messages.success(request, "Estudante cadastrado com sucesso!")
      return redirect('login')
      # except Exception as e:
      #     messages.error(request, "Erro ao cadastrar Estudante!!")
      #     return render(request, 'pages/register.html')
    else:
        return render(request, 'pages/register.html')