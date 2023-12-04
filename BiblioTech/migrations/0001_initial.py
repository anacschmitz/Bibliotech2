# Generated by Django 4.2.6 on 2023-10-27 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Genders',
            },
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeLivro', models.CharField(max_length=255)),
                ('qtdPaginas', models.IntegerField()),
                ('capaLivro', models.ImageField(upload_to='')),
                ('autor', models.CharField(max_length=255)),
                ('qtdLivros', models.IntegerField()),
                ('estudanteSacado', models.CharField(max_length=255)),
                ('generoLivro', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='BiblioTech.genero')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]