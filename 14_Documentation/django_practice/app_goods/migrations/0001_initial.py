# Generated by Django 2.2 on 2022-06-03 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='название')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('weight', models.FloatField(verbose_name='вес')),
            ],
        ),
    ]
