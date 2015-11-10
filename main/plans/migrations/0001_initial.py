# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Название плана тестирования')),
                ('stand_url', models.CharField(max_length=50, verbose_name='Адрес стенда, на котором проверяем')),
                ('stand_user', models.CharField(max_length=50, verbose_name='Пользователь, под которым проводится проверка')),
                ('date', models.DateTimeField(verbose_name='Дата создания плана')),
                ('text', models.TextField(verbose_name='Текст плана')),
            ],
            options={
                'verbose_name_plural': 'Тестовые планы',
                'verbose_name': 'Тестовые план',
                'db_table': 'plans',
            },
        ),
        migrations.CreateModel(
            name='Processes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Название процесса')),
            ],
            options={
                'verbose_name_plural': 'Процессы',
                'verbose_name': 'Процесс',
                'db_table': 'processes',
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Название вида деятельности')),
            ],
            options={
                'verbose_name_plural': 'Виды деятельности',
                'verbose_name': 'Вид деятельности',
                'db_table': 'species',
            },
        ),
        migrations.AddField(
            model_name='processes',
            name='species',
            field=models.ForeignKey(to='plans.Species'),
        ),
        migrations.AddField(
            model_name='plans',
            name='process',
            field=models.ForeignKey(to='plans.Processes'),
        ),
        migrations.AddField(
            model_name='plans',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
