# Generated by Django 4.2.6 on 2023-11-30 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_estudante_matriculaestudante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudante',
            name='password',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
