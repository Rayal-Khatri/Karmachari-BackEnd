# Generated by Django 4.1.4 on 2023-02-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_rename_name_notice_username_alter_notice_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ph_no',
            field=models.IntegerField(default=0),
        ),
    ]
