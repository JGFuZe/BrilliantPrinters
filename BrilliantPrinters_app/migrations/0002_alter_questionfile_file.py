# Generated by Django 4.2.6 on 2023-11-25 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BrilliantPrinters_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionfile',
            name='file',
            field=models.FileField(null=True, upload_to='documents/%Y/%m/%d'),
        ),
    ]
