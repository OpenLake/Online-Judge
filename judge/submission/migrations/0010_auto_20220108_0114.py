# Generated by Django 3.1.1 on 2022-01-08 01:14

from django.db import migrations, models
import submission.utils


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0009_auto_20220108_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='code_file',
            field=models.FileField(upload_to=submission.utils.code_file_name),
        ),
    ]
