# Generated by Django 4.1.5 on 2023-02-03 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0003_auto_20230203_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dnevnik',
            name='trainings',
        ),
    ]