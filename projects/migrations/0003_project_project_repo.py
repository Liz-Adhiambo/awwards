# Generated by Django 4.0.5 on 2022-06-11 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_project_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_repo',
            field=models.URLField(blank=True, null=True),
        ),
    ]
