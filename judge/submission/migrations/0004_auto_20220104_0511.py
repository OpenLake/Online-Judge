# Generated by Django 3.1.1 on 2022-01-04 05:11

from django.db import migrations, models
import submission.utils


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0003_auto_20220103_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='code_file',
            field=models.FileField(upload_to=submission.utils.code_file_name),
        ),
    ]
