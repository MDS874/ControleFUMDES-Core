# Generated by Django 5.0.9 on 2024-11-25 22:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comprovantes', '0002_comprovantecomentario'),
        ('core', '0002_aluno_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprovante',
            name='idAluno',
            field=models.ForeignKey(db_column='idAluno', on_delete=django.db.models.deletion.CASCADE, to='core.aluno'),
        ),
    ]
