# Generated by Django 3.2.17 on 2023-02-25 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='checkOutTime',
            field=models.DateTimeField(null=True),
        ),
    ]
