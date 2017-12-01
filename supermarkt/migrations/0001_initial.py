# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-01 20:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'webgis_company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.CharField(blank=True, max_length=200, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supermarkt.Company')),
            ],
            options={
                'db_table': 'webgis_produkt',
                'verbose_name_plural': 'Produkte',
            },
        ),
        migrations.CreateModel(
            name='ProduktType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'webgis_produkttype',
                'verbose_name_plural': 'Produkttypen',
            },
        ),
        migrations.AddField(
            model_name='produkt',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supermarkt.ProduktType'),
        ),
    ]
