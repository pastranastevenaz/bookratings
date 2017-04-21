# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 23:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='comment',
        ),
        migrations.AddField(
            model_name='bookcomment',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Book'),
        ),
    ]