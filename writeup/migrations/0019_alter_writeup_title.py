# Generated by Django 4.0.2 on 2022-02-18 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writeup', '0018_cate_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writeup',
            name='title',
            field=models.TextField(),
        ),
    ]
