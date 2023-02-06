# Generated by Django 4.1.4 on 2023-02-05 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_profile_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='body',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='username',
        ),
        migrations.AddField(
            model_name='notice',
            name='context',
            field=models.TextField(default='00', max_length=100000),
        ),
        migrations.AddField(
            model_name='notice',
            name='department',
            field=models.CharField(default='All Departments', max_length=100),
        ),
        migrations.AddField(
            model_name='notice',
            name='sn',
            field=models.IntegerField(default=0),
        ),
    ]