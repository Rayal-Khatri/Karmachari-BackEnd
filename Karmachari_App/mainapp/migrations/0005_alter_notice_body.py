# Generated by Django 4.1.5 on 2023-02-05 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='body',
            field=models.TextField(max_length=100000),
        ),
    ]
