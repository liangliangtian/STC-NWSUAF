# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-07-11 08:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('share', '0001_initial'),
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('content', models.ImageField(blank=True, default='', upload_to='static/upload/evidence')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.User')),
            ],
            options={
                'ordering': ['create_time'],
                'verbose_name': '证据',
                'verbose_name_plural': '证据',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_type', models.IntegerField(choices=[(0, '支付问题'), (1, '其他')])),
                ('is_ongoing', models.BooleanField(default=True)),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('info', models.CharField(max_length=200)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.User')),
            ],
            options={
                'ordering': ['create_time'],
                'verbose_name': '投诉',
                'verbose_name_plural': '投诉',
            },
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, default='', upload_to='static/upload/alipay')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='商品价格')),
                ('pay_way', models.IntegerField(choices=[(0, '支付宝'), (1, '微信'), (2, '当面交易')])),
                ('pay_pic', models.ImageField(blank=True, default='', upload_to='static/upload/alipay')),
                ('info', models.CharField(max_length=200)),
                ('sell_times', models.IntegerField(default=0)),
                ('isfile', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='index.User', verbose_name='创建者')),
                ('file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='share.File')),
            ],
            options={
                'ordering': ['create_time'],
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
            },
        ),
        migrations.CreateModel(
            name='GoodRemark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('remark_type', models.IntegerField(choices=[(0, '好评'), (1, '差评')])),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.User')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Good')),
            ],
            options={
                'ordering': ['create_time'],
                'verbose_name': '商品评论',
                'verbose_name_plural': '商品评论',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.IntegerField(choices=[(0, '等待支付'), (1, '等待卖家确认'), (2, '交易完成'), (3, '投诉中'), (4, '交易取消')])),
                ('buyer_ok', models.BooleanField(default=False)),
                ('seller_ok', models.BooleanField(default=False)),
                ('buyer_marked', models.BooleanField(default=False)),
                ('seller_marked', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.User')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Good')),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
            },
        ),
        migrations.CreateModel(
            name='TradeMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('mark_type', models.IntegerField(choices=[(0, '好评'), (1, '差评')])),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.User')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Order')),
            ],
            options={
                'ordering': ['create_time'],
                'verbose_name': '交易评论',
                'verbose_name_plural': '交易评论',
            },
        ),
        migrations.CreateModel(
            name='TradeMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('content', models.CharField(max_length=200)),
                ('have_read', models.BooleanField(default=False)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Order')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='index.User')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='index.User')),
            ],
            options={
                'ordering': ['create_time'],
                'verbose_name': '交易消息',
                'verbose_name_plural': '交易消息',
            },
        ),
        migrations.AddField(
            model_name='feedback',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Order'),
        ),
        migrations.AddField(
            model_name='evidence',
            name='feedback',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Feedback'),
        ),
    ]
