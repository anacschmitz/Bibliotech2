from django.contrib.auth.models import AbstractUser
from django.db import models


class Estudante(models.Model):
    nomeEstudante = models.CharField(max_length=255, blank=True)
    cpf = models.CharField(max_length=11, blank=True, unique=True)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    cep = models.CharField(max_length=8)
    password = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=45, blank=True)
    matriculaEstudante = models.CharField(max_length=6, blank=True, unique=True)
    curso = models.CharField(max_length=255)

    def __str__(self):
        return self.nomeEstudante

    class Meta:
        verbose_name = 'Estudante'
        verbose_name_plural = 'Estudantes'


class CustomUser(AbstractUser):
    estudante = models.OneToOneField(Estudante, on_delete=models.CASCADE, null=True, blank=True)