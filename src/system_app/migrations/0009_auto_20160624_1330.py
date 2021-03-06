# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-24 11:30
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system_app', '0008_auto_20160622_1907'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deszcz',
            options={'verbose_name': 'Stopie\u0144 deszczu', 'verbose_name_plural': 'Stopnie deszczu'},
        ),
        migrations.AlterModelOptions(
            name='lawina',
            options={'verbose_name': 'Stopie\u0144 lawiny', 'verbose_name_plural': 'Stopnie lawiny'},
        ),
        migrations.AlterModelOptions(
            name='mgla',
            options={'verbose_name': 'Stopie\u0144 mg\u0142y', 'verbose_name_plural': 'Stopnie mg\u0142y'},
        ),
        migrations.AlterModelOptions(
            name='pogoda',
            options={'verbose_name': 'Pogoda', 'verbose_name_plural': 'Pogody'},
        ),
        migrations.AlterModelOptions(
            name='stanalarmowy',
            options={'verbose_name': 'Stan alarmowy', 'verbose_name_plural': 'Stany alarmowe'},
        ),
        migrations.AlterModelOptions(
            name='strefazagrozenia',
            options={'verbose_name': 'Strefa zagro\u017cenia', 'verbose_name_plural': 'Strefy zagro\u017cenia'},
        ),
        migrations.AlterModelOptions(
            name='szlak',
            options={'verbose_name': 'Szlak', 'verbose_name_plural': 'Szlaki'},
        ),
        migrations.AlterModelOptions(
            name='temperatura',
            options={'verbose_name': 'Stopie\u0144 temperatury', 'verbose_name_plural': 'Stopnie temperatury'},
        ),
        migrations.AlterModelOptions(
            name='wiatr',
            options={'verbose_name': 'Stopie\u0144 wiatru', 'verbose_name_plural': 'Stopnie wiatru'},
        ),
        migrations.AlterField(
            model_name='deszcz',
            name='deszcz_maksymalny',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Deszcz maksymalny'),
        ),
        migrations.AlterField(
            model_name='deszcz',
            name='deszcz_minimalny',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Deszcz minimanly'),
        ),
        migrations.AlterField(
            model_name='deszcz',
            name='stopien',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Stopie\u0144'),
        ),
        migrations.AlterField(
            model_name='deszcz',
            name='wiatr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_app.Wiatr', verbose_name='Wiatr'),
        ),
        migrations.AlterField(
            model_name='lawina',
            name='opis',
            field=models.TextField(verbose_name='Opis'),
        ),
        migrations.AlterField(
            model_name='lawina',
            name='stopien',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Stopie\u0144'),
        ),
        migrations.AlterField(
            model_name='mgla',
            name='opis',
            field=models.TextField(verbose_name='Opis'),
        ),
        migrations.AlterField(
            model_name='mgla',
            name='stopien',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Stopie\u0144'),
        ),
        migrations.AlterField(
            model_name='pogoda',
            name='czas',
            field=models.DateTimeField(verbose_name='Czas'),
        ),
        migrations.AlterField(
            model_name='pogoda',
            name='deszcz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_app.Deszcz', verbose_name='Stopie\u0144 deszczu'),
        ),
        migrations.AlterField(
            model_name='pogoda',
            name='lawina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_app.Lawina', verbose_name='Stopie\u0144 lawiny'),
        ),
        migrations.AlterField(
            model_name='pogoda',
            name='mgla',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_app.Mgla', verbose_name='Stopie\u0144 mg\u0142y'),
        ),
        migrations.AlterField(
            model_name='pogoda',
            name='szlak',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system_app.Szlak', verbose_name='Szlak'),
        ),
        migrations.AlterField(
            model_name='pogoda',
            name='temperatura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_app.Temperatura', verbose_name='Stopie\u0144 temperatury'),
        ),
        migrations.AlterField(
            model_name='pogoda',
            name='wiatr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_app.Wiatr', verbose_name='Stopie\u0144 wiatru'),
        ),
        migrations.AlterField(
            model_name='stanalarmowy',
            name='dzialanie',
            field=models.CharField(choices=[('sm', 'System monitoruje'), ('mt', 'Monitorowanie turyst\xf3w na zagro\u017conych obszarach'), ('wd', 'Wys\u0142anie drona w celu lepszego monitorowania szlaku'), ('wder', 'Wys\u0142anie drona do zbadania sytuacji i podj\u0119cia decyzji o wys\u0142aniu ekipy ratowniczej'), ('pt', 'Przechwycenie turyst\xf3w')], default='sm', max_length=255, verbose_name='Dzia\u0142anie'),
        ),
        migrations.AlterField(
            model_name='stanalarmowy',
            name='poziom',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Poziom'),
        ),
        migrations.AlterField(
            model_name='strefazagrozenia',
            name='nazwa',
            field=models.CharField(max_length=255, verbose_name='Nazwa'),
        ),
        migrations.AlterField(
            model_name='strefazagrozenia',
            name='pozycja_E',
            field=models.FloatField(verbose_name='Pozycja E'),
        ),
        migrations.AlterField(
            model_name='strefazagrozenia',
            name='pozycja_N',
            field=models.FloatField(verbose_name='Pozycja N'),
        ),
        migrations.AlterField(
            model_name='strefazagrozenia',
            name='promien',
            field=models.IntegerField(help_text='jednostka [m]', verbose_name='Promie\u0144'),
        ),
        migrations.AlterField(
            model_name='szlak',
            name='kolor',
            field=models.CharField(choices=[('zo', '\u017c\xf3\u0142ty'), ('n', 'niebieski'), ('z', 'zielony'), ('cza', 'czarny'), ('cze', 'czerwony')], max_length=255, verbose_name='Kolor'),
        ),
        migrations.AlterField(
            model_name='szlak',
            name='nazwa',
            field=models.CharField(max_length=255, verbose_name='Nazwa'),
        ),
        migrations.AlterField(
            model_name='szlak',
            name='stan_alarmowy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_app.StanAlarmowy', verbose_name='Stan alarmowy'),
        ),
        migrations.AlterField(
            model_name='szlak',
            name='trudnosc',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Trudno\u015b\u0107'),
        ),
        migrations.AlterField(
            model_name='temperatura',
            name='ponizej',
            field=models.IntegerField(verbose_name='Poni\u017cej'),
        ),
        migrations.AlterField(
            model_name='temperatura',
            name='powyzej',
            field=models.IntegerField(verbose_name='Powy\u017cej'),
        ),
        migrations.AlterField(
            model_name='temperatura',
            name='stopien',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Stopie\u0144'),
        ),
        migrations.AlterField(
            model_name='wiatr',
            name='predkosc_maksymalna',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Pr\u0119dko\u015b\u0107 maksymalna'),
        ),
        migrations.AlterField(
            model_name='wiatr',
            name='predkosc_minimalna',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Pr\u0119dko\u015b\u0107 minimalna'),
        ),
        migrations.AlterField(
            model_name='wiatr',
            name='stopien',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Stopie\u0144'),
        ),
    ]
