# Generated by Django 4.1.5 on 2023-03-12 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_alter_payroll_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payroll',
            name='overtime_multiplier',
        ),
    ]
