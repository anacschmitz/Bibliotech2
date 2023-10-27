from django.contrib import admin
from .models import Livro, Genero

# Custom admin class for Livro model
class LivroAdmin(admin.ModelAdmin):
    list_display = ['nomeLivro', 'generoLivro', 'qtdPaginas', 'capaLivro', 'autor', 'qtdLivros', 'estudanteSacado']


admin.site.register(Livro, LivroAdmin)
admin.site.register(Genero)
