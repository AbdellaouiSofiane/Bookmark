# Generated by Django 3.2 on 2021-04-24 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_logout',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
