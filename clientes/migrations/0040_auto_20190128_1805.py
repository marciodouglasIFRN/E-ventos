# Generated by Django 2.1.4 on 2019-01-28 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0039_auto_20190128_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='token',
            field=models.CharField(blank=True, default=191289, max_length=14, null=True),
        ),
    ]
