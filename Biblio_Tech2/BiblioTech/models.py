from django.db import models

# Create your models here.
class Genero(models.Model):
    genero = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.genero

    class Meta:
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'

class Livro(models.Model):
    nomeLivro = models.CharField(max_length=255)
    generoLivro = models.ForeignKey(Genero, on_delete = models.CASCADE, blank=True)
    qtdPaginas = models.IntegerField()
    capaLivro = models.ImageField(blank=False)
    autor = models.CharField(max_length=255)
    qtdLivros = models.IntegerField()
    estudanteSacado = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.nomeLivro

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

# class Estudante(models.Model):
#     nomeEstudante = models.CharField(max_length=255)
#     matriculaEstudante = models.IntegerField(max_length=6)
#     curso = models.CharField(max_length=255)





