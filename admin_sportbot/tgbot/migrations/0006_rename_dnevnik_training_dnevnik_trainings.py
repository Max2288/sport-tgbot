# Generated by Django 4.1.5 on 2023-02-03 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0005_dnevnik_trainings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dnevnik_training',
            new_name='Dnevnik_trainings',
        ),
    ]
