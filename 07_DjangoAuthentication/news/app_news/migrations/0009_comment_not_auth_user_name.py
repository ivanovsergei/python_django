# Generated by Django 2.2 on 2022-04-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0008_auto_20220401_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='not_auth_user_name',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
    ]
