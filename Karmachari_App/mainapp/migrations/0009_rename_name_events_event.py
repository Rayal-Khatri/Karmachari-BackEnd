# Generated by Django 3.2.17 on 2023-03-11 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_allowedip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='name',
            new_name='event',
        ),
    ]
