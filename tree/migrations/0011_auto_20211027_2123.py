# Generated by Django 2.2 on 2021-10-27 13:23

from django.db import migrations, models
import tree.models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0010_auto_20211027_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='File_name',
        ),
        migrations.AlterField(
            model_name='node',
            name='File',
            field=models.FileField(default='', null=True, upload_to=tree.models.get_file_upload_path, verbose_name='文件路径'),
        ),
    ]
