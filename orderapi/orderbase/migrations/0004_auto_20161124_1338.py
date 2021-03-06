# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-24 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderbase', '0003_auto_20161116_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('photo', models.FileField(upload_to=b'image')),
                ('description', models.TextField(blank=True)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('loaded', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'media_photos',
            },
        ),
        migrations.RemoveField(
            model_name='merchandise',
            name='image',
        ),
    ]
