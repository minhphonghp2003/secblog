# Generated by Django 4.0.2 on 2022-02-13 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writeup', '0004_alter_writeup_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='writeup',
            name='cate',
            field=models.CharField(choices=[('pwnable.kr', 'pwnable.kr'), ('ctf', 'ctf')], default='challenge', max_length=100),
        ),
    ]
