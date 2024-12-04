# Generated by Django 5.0.9 on 2024-11-26 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comprovantes', '0003_alter_comprovante_idaluno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprovante',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Reprovado')], default=0),
        ),
    ]
