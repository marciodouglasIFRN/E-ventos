# Generated by Django 2.1.4 on 2018-12-27 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0006_auto_20181227_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='promotores',
            field=models.ManyToManyField(blank=True, null=True, to='promotor.PromotorEventos'),
        ),
    ]
