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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Название плана тестирования', max_length=200)),
                ('stand_url', models.CharField(verbose_name='Адрес стенда, на котором проверяем', max_length=50)),
                ('stand_user', models.CharField(verbose_name='Пользователь, под которым проводится проверка', max_length=50)),
                ('date', models.DateTimeField(verbose_name='Дата создания плана')),
                ('text', models.TextField(verbose_name='Текст плана')),
            ],
            options={
                'verbose_name_plural': 'Тестовые планы',
                'db_table': 'plans',
                'verbose_name': 'Тестовые план',
            },
        ),
        migrations.CreateModel(
            name='Processes',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Название процесса', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Процессы',
                'db_table': 'processes',
                'verbose_name': 'Процесс',
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Название вида деятельности', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Виды деятельности',
                'db_table': 'species',
                'verbose_name': 'Вид деятельности',
            },
        ),
        migrations.AddField(
            model_name='processes',
            name='species',
            field=models.ForeignKey(to='plans.Species', verbose_name='Вид деятельности'),
        ),
        migrations.AddField(
            model_name='plans',
            name='process',
            field=models.ForeignKey(to='plans.Processes', verbose_name='Процесс'),
        ),
        migrations.AddField(
            model_name='plans',
            name='species',
            field=models.ForeignKey(to='plans.Species', verbose_name='Вид деятельности'),
        ),
        migrations.AddField(
            model_name='plans',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
