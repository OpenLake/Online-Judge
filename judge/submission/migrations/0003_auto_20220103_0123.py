# Generated by Django 3.1.1 on 2022-01-03 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0002_auto_20220103_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='code_file',
            field=models.FileField(upload_to='code'),
        ),
    ]
