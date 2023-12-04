from django.db import models
from accounts.models import CustomUser


class Genero(models.Model):
    genero = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.genero

    class Meta:
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'


class Livro(models.Model):
    estudante = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default='1')
    nomeLivro = models.CharField(max_length=255)
    generoLivro = models.ForeignKey(Genero, on_delete=models.CASCADE, blank=True)
    qtdPaginas = models.IntegerField()
    capaLivro = models.ImageField(blank=False)
    autor = models.CharField(max_length=255)
    qtdLivros = models.IntegerField()
    qtdLivrosEstoque = models.CharField(max_length=3, blank=False)

    def __str__(self) -> str:
        return self.nomeLivro

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Historico(models.Model):
    estudante = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, blank=True)
    emprestado = models.BooleanField(blank=True)
    atraso = models.BooleanField(blank=True)
    data_emprestimo = models.DateField(blank=True)
    data_devolucao = models.DateField(blank=True)

    def __str__(self) -> bool:
        return self.emprestado

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'











