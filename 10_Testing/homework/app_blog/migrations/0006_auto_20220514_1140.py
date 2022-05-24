# Generated by Django 2.2 on 2022-05-14 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0005_auto_20220514_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='filename',
            field=models.CharField(default=1, max_length=30, verbose_name='Название файла'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_users.Profile', verbose_name='Автор статьи'),
        ),
    ]
