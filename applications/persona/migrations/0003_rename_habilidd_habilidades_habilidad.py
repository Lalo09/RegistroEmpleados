# Generated by Django 3.2.7 on 2021-09-08 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_auto_20210908_0359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habilidades',
            old_name='habilidd',
            new_name='habilidad',
        ),
    ]
