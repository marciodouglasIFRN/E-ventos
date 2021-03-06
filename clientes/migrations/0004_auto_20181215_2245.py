# Generated by Django 2.1.4 on 2018-12-15 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20181211_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='complemento',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='pessoa',
            old_name='logradouro',
            new_name='rua',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='apelido',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='senha',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='matricula',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='sobrenome',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='alunos_photos'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='token',
            field=models.CharField(blank=True, default=958629, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
