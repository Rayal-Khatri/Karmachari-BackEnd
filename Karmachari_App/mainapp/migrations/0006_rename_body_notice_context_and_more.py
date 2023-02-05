# Generated by Django 4.1.5 on 2023-02-05 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_notice_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='body',
            new_name='context',
        ),
        migrations.RenameField(
            model_name='notice',
            old_name='username',
            new_name='department',
        ),
        migrations.AddField(
            model_name='notice',
            name='sn',
            field=models.IntegerField(default=1),
        ),
    ]