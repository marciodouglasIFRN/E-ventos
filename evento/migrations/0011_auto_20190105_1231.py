# Generated by Django 2.1.4 on 2019-01-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0017_auto_20190105_1231'),
        ('evento', '0010_auto_20190105_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingresso',
            name='pk_aluno',
        ),
        migrations.AddField(
            model_name='ingresso',
            name='aluno',
            field=models.ManyToManyField(blank=True, null=True, to='clientes.Aluno'),
        ),
    ]