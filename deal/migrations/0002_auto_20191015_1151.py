# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-10-15 03:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stocks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='selfstock',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='dealstock',
            name='buser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buser', to=settings.AUTH_USER_MODEL, verbose_name='买家'),
        ),
        migrations.AddField(
            model_name='dealstock',
            name='suser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suser', to=settings.AUTH_USER_MODEL, verbose_name='卖家'),
        ),
        migrations.AddField(
            model_name='bosstock',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.Stock', verbose_name='股票'),
        ),
        migrations.AddField(
            model_name='bosstock',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
