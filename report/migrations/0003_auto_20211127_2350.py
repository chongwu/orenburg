# Generated by Django 3.2.9 on 2021-11-27 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20211127_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='world',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='world_letter_designation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
