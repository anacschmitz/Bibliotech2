from django.shortcuts import render
from .models import Livro, Genero

def index(request):
  #from Products select *
  livros = Livro.objects.all()
  # for produto in produtos:
  #   print(f'{produto.name} + {produto.price}')

  # return render(request, 'pages/index.html', {'books':produtos})
  return render(request, 'pages/index.html')





# Create your views here.
# def add_estudante(request):
    # if request.method == 'POST':
    #     nomeLivro = request.POST.get('nomeLivro')
    #     generoLivro = request.POST.get('generoLivro')
    #     qtdPaginas =
    #
    #     picture = request.FILES.get('picture')
    #     price = request.POST.get('price')
    #     description = request.POST.get('description')
    #     qtd = request.POST.get('qtd')
    #     discount = request.POST.get('discount')
    #     created_at = datetime.now()
    #     in_stock = True
