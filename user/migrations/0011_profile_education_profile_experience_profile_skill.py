# Generated by Django 4.0.2 on 2022-02-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_profile_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.ManyToManyField(to='user.Education'),
        ),
        migrations.AddField(
            model_name='profile',
            name='experience',
            field=models.ManyToManyField(to='user.Experience'),
        ),
        migrations.AddField(
            model_name='profile',
            name='skill',
            field=models.ManyToManyField(to='user.Skill'),
        ),
    ]
