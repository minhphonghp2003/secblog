# Generated by Django 4.0.2 on 2022-02-13 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_alter_skill_skill_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='about_fb',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='about_ins',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='about_phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='about_zl',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]