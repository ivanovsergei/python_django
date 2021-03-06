# Generated by Django 2.2 on 2022-05-30 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_shops', '0002_auto_20220530_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='balance', to='app_shops.Client', verbose_name='Пользователь'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offers',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='app_shops.Client', verbose_name='Пользователь'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymenthistory',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='payment_history', to='app_shops.Client', verbose_name='Пользователь'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='balance',
            name='balance',
            field=models.IntegerField(default=100, null=True),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='price',
            field=models.IntegerField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotions', to='app_shops.Client', verbose_name='Пользователь'),
        ),
    ]
