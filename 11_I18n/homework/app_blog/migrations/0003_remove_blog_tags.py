# Generated by Django 2.2 on 2022-05-13 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_auto_20220513_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='tags',
        ),
    ]
