# Generated by Django 2.2 on 2021-10-27 10:00

from django.db import migrations, models
import tree.models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0009_node_file_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='File_path',
        ),
        migrations.AddField(
            model_name='node',
            name='File',
            field=models.FileField(default='unamed', null=True, upload_to=tree.models.get_file_upload_path, verbose_name='文件路径'),
        ),
        migrations.AlterField(
            model_name='node',
            name='File_name',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='文件名'),
        ),
    ]
