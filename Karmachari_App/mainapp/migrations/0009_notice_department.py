# Generated by Django 4.1.5 on 2023-02-05 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_remove_notice_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='department',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]