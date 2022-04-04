# Generated by Django 2.2 on 2022-03-28 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0006_auto_20220322_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('a', 'Активен'), ('d', 'Удалено Администратором')], default='a', max_length=1, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Имя пользователя'),
        ),
    ]