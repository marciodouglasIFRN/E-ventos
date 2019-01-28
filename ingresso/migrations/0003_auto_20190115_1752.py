# Generated by Django 2.1.4 on 2019-01-15 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0013_auto_20190114_1310'),
        ('ingresso', '0002_auto_20190115_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingresso',
            name='evento',
        ),
        migrations.AddField(
            model_name='ingresso',
            name='evento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='evento.Evento'),
        ),
    ]