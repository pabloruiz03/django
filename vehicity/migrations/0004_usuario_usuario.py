# Generated by Django 4.1.6 on 2023-02-26 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicity', '0003_usuario_confirmacion_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='usuario',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
