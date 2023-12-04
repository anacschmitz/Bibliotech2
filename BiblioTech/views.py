from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from BiblioTech.models import Livro, Historico
from accounts.models import CustomUser
from datetime import date, timedelta
from django.db.models import F


def index(request):
    livros = Livro.objects.all()
    return render(request, 'pages/index.html', {'livros': livros})

def search_book(request):
    q = request.GET.get('q')
    livros = Livro.objects.filter(nomeLivro__icontains=q)
    return render(request, 'pages/index.html', {'livros': livros})


def book_detail(request, id):
    livro = Livro.objects.get(id=id)
    return render(request, 'pages/book_detail.html', {'livro': livro})


def emprestar(request, id):
    livro = Livro.objects.get(id=id)
    estudante = request.user
    consultar = Historico.objects.filter(estudante=estudante.id, livro=livro.id)
    emprestimo = consultar.last()
    if consultar.exists() and emprestimo.emprestado:
        messages.success(request, "Você já está com o livro solicitado!")
    else:
        if livro.qtdLivros > 0:
            Historico.objects.create(estudante=estudante, livro=livro, emprestado=True, atraso=False,
                                     data_emprestimo=date.today(),
                                     data_devolucao=(date.today() + timedelta(days=10)))
            messages.success(request, "Livro Emprestado!")
            Livro.objects.filter(id=id).update(qtdLivros=F('qtdLivros') - 1)
    return redirect('book-detail', id)


def devolver(request, id):
    livro = Livro.objects.get(id=id)
    estudante = request.user
    consultar = Historico.objects.filter(estudante=estudante.id, livro=livro.id, emprestado=True)
    emprestimo = consultar.last()
    if emprestimo and livro.qtdLivros < int(livro.qtdLivrosEstoque):
        Historico.objects.filter(estudante=estudante.id, livro=livro.id).update(emprestado=False)
        messages.success(request, "Livro Devolvido!")
        Livro.objects.filter(id=id).update(qtdLivros=F('qtdLivros') + 1)
    else:
        messages.success(request, "Você não tem esse livro para devolver")
    return redirect('book-detail', id)