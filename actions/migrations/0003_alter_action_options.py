# Generated by Django 3.2 on 2021-04-24 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0002_rename_action_action_verb'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='action',
            options={'ordering': ('-created',)},
        ),
    ]
