# Generated by Django 2.1 on 2018-09-12 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_transacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='transacao',
            name='catergoria',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cliente.Caregoria'),
            preserve_default=False,
        ),
    ]
