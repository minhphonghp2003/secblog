# Generated by Django 4.0.2 on 2022-02-12 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_profile_education_alter_profile_experience_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='user',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='education',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='skill',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='user',
        ),
        migrations.AddField(
            model_name='education',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='edu', to='user.profile'),
        ),
        migrations.AddField(
            model_name='experience',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exp', to='user.profile'),
        ),
        migrations.AddField(
            model_name='skill',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skill', to='user.profile'),
        ),
    ]
