# Generated by Django 3.2.7 on 2021-09-08 04:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_rename_habilidd_habilidades_habilidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default='-'),
            preserve_default=False,
        ),
    ]
