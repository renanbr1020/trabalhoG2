# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 22:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0013_remove_institucional_descricao_do_feriado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Privada',
            fields=[
                ('agenda_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='agenda.Agenda')),
                ('descricao_Da_Agenda', models.TextField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.Usuario')),
            ],
            bases=('agenda.agenda',),
        ),
    ]