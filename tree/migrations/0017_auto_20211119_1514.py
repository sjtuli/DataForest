# Generated by Django 2.2 on 2021-11-19 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0016_auto_20211029_1929'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': '路径树', 'verbose_name_plural': '路径树'},
        ),
        migrations.AlterModelOptions(
            name='node',
            options={'verbose_name': '叶子节点', 'verbose_name_plural': '叶子节点'},
        ),
        migrations.AlterModelOptions(
            name='nodefile',
            options={'verbose_name': '上传文件', 'verbose_name_plural': '上传文件'},
        ),
    ]
