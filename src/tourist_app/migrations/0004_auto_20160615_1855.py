# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-15 16:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0003_auto_20160525_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.TextField()),
                ('lider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tourist_app.Turysta')),
            ],
            options={
                'verbose_name_plural': 'Grupy',
            },
        ),
        migrations.CreateModel(
            name='ZagrozenieTurysty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zagrozenie', models.CharField(choices=[('np', 'Mozliwe zaslabniecie, wyslij drona'), ('sz', 'Turysta w strefie zagrozenia'), ('oog', 'Turysta oddalil sie od lidera grupy')], max_length=255)),
                ('turysta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourist_app.Turysta')),
            ],
            options={
                'verbose_name_plural': 'Zagrozenia turystow',
            },
        ),
        migrations.AddField(
            model_name='turysta',
            name='grupa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tourist_app.Grupa'),
        ),
    ]
