# Generated by Django 2.1.4 on 2019-01-03 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0012_auto_20181227_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='token',
            field=models.CharField(blank=True, default=333997, max_length=14, null=True),
        ),
    ]