# Generated by Django 4.0.2 on 2022-02-13 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_alter_profile_background_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill_progress',
            field=models.DecimalField(decimal_places=0, max_digits=2, null=True),
        ),
    ]
