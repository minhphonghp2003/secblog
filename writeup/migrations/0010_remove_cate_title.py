# Generated by Django 4.0.2 on 2022-02-13 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writeup', '0009_delete_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cate',
            name='title',
        ),
    ]
