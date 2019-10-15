# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-10-15 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='标题')),
                ('callback_url', models.URLField(blank=True, null=True, verbose_name='url地址')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stonumber', models.CharField(max_length=20, verbose_name='股票编码')),
                ('company_name', models.CharField(max_length=64, verbose_name='公司名称')),
                ('industry', models.CharField(blank=True, max_length=200, null=True, verbose_name='细分行业')),
                ('area', models.CharField(blank=True, max_length=30, null=True, verbose_name='地区')),
                ('pe', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='市盈率')),
                ('outstanding', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='流通股本(亿)')),
                ('totals', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='总股本(亿)')),
                ('totalAssets', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='总资产(万)')),
                ('liquidAssets', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='流动资产')),
                ('fixedAssets', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='固定资产')),
                ('reserved', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='公积金')),
                ('reservedPerShare', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='每股公积金')),
                ('esp', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='每股收益')),
                ('bvps', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='每股净资')),
                ('pb', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='市净率')),
                ('timeToMarket', models.DateField(verbose_name='上市日期')),
            ],
            options={
                'verbose_name': '股票信息',
                'verbose_name_plural': '股票信息',
                'db_table': 'Stock',
                'ordering': ['-id'],
            },
        ),
    ]
