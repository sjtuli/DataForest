# Generated by Django 2.2 on 2021-10-27 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0011_auto_20211027_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='File_name',
            field=models.CharField(default='', max_length=128, null=True, verbose_name='文件名'),
        ),
    ]