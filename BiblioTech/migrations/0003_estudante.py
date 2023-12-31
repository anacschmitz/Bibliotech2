# Generated by Django 4.2.6 on 2023-11-30 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BiblioTech', '0002_alter_livro_estudantesacado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeEstudante', models.CharField(blank=True, max_length=255)),
                ('cpf', models.CharField(blank=True, max_length=11, unique=True)),
                ('rua', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=8)),
                ('password', models.CharField(blank=True, max_length=10, unique=True)),
                ('email', models.CharField(blank=True, max_length=45)),
                ('matriculaEstudante', models.IntegerField(blank=True, max_length=6, unique=True)),
                ('curso', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Estudante',
                'verbose_name_plural': 'Estudantes',
            },
        ),
    ]
