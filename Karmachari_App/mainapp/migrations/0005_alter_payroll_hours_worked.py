# Generated by Django 4.1.5 on 2023-03-06 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_payroll_hours_worked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='hours_worked',
            field=models.FloatField(blank=True, default=10),
        ),
    ]
