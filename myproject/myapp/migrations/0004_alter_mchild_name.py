# Generated by Django 4.1.3 on 2022-11-17 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_mchild_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mchild',
            name='name',
            field=models.TextField(null=True),
        ),
    ]