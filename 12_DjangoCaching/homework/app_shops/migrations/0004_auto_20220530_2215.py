# Generated by Django 2.2 on 2022-05-30 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_shops', '0003_auto_20220530_2211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='balance',
            old_name='balance',
            new_name='total',
        ),
    ]