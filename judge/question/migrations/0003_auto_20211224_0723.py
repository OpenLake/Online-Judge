# Generated by Django 3.1.1 on 2021-12-24 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_test'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='test',
            options={'verbose_name': 'Test', 'verbose_name_plural': 'Tests'},
        ),
        migrations.AlterField(
            model_name='test',
            name='input_file',
            field=models.FilePathField(match='input_file*', path='test'),
        ),
        migrations.AlterField(
            model_name='test',
            name='output_file',
            field=models.FilePathField(match='output_file*', path='test'),
        ),
    ]
