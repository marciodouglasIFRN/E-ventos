# Generated by Django 2.1.4 on 2019-01-14 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0012_remove_ingresso_promotores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingresso',
            name='aluno',
        ),
        migrations.RemoveField(
            model_name='ingresso',
            name='evento',
        ),
        migrations.DeleteModel(
            name='Ingresso',
        ),
    ]
