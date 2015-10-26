# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Заголовок тест кейса', max_length=200)),
                ('date', models.DateTimeField(verbose_name='Дата создания тестового сценария')),
                ('text', models.TextField(verbose_name='Текст кейса')),
            ],
            options={
                'db_table': 'cases',
            },
        ),
    ]
