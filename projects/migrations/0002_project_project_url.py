# Generated by Django 4.0.5 on 2022-06-11 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Project_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
