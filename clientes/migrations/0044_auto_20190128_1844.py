# Generated by Django 2.1.4 on 2019-01-28 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0043_auto_20190128_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='token',
            field=models.CharField(blank=True, default=620114, max_length=14, null=True),
        ),
    ]