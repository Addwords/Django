# Generated by Django 4.1.3 on 2022-11-22 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_mchild_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mchild',
            name='height',
        ),
    ]
