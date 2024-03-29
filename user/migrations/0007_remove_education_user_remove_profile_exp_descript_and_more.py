# Generated by Django 4.0.2 on 2022-02-11 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_education_prof_education_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='exp_descript',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='exp_title',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='exp_year',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='skill_progress',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='skill_title',
        ),
        migrations.AddField(
            model_name='education',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_title', models.CharField(max_length=100, null=True)),
                ('skill_progress', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_title', models.CharField(max_length=100, null=True)),
                ('exp_year', models.DateField(null=True)),
                ('exp_descript', models.TextField(null=True)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
        ),
    ]
