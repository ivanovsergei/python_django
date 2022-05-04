# Generated by Django 2.2 on 2022-04-05 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активность')),
                ('title', models.CharField(max_length=30, verbose_name='Заголовок')),
                ('description', models.TextField(default='', verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('published_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'вакансия',
                'verbose_name_plural': 'вакансии',
                'permissions': (('can_publish', 'может публиковать'),),
            },
        ),
    ]