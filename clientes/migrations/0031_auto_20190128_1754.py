# Generated by Django 2.1.4 on 2019-01-28 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0030_auto_20190126_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='token',
            field=models.CharField(blank=True, default=569638, max_length=14, null=True),
        ),
    ]
