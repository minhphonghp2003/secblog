# Generated by Django 4.0.2 on 2022-02-12 05:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0014_remove_education_user_remove_experience_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='profile',
        ),
        migrations.AddField(
            model_name='education',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='edu', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='experience',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exp', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='skill',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skill', to=settings.AUTH_USER_MODEL),
        ),
    ]