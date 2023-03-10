# Generated by Django 4.1.5 on 2023-03-10 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_payroll_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='net_pay',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8),
        ),
    ]
