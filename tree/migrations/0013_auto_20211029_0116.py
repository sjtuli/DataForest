# Generated by Django 2.2 on 2021-10-28 17:16

from django.db import migrations, models
import django.db.models.deletion
import tree.models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0012_node_file_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': '树', 'verbose_name_plural': '树'},
        ),
        migrations.AlterModelOptions(
            name='node',
            options={'verbose_name': '节点', 'verbose_name_plural': '节点'},
        ),
        migrations.RemoveField(
            model_name='node',
            name='File',
        ),
        migrations.RemoveField(
            model_name='node',
            name='File_name',
        ),
        migrations.AlterField(
            model_name='department',
            name='question',
            field=models.ForeignKey(default=3, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department', to='QuestionApp.Question', verbose_name='关联实验'),
        ),
        migrations.AlterField(
            model_name='node',
            name='body',
            field=models.TextField(default='', verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='node',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='node', to='tree.Department', verbose_name='节点'),
        ),
        migrations.CreateModel(
            name='NodeFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File', models.FileField(default='', null=True, upload_to=tree.models.get_file_upload_path, verbose_name='文件路径')),
                ('File_name', models.CharField(default='', max_length=128, null=True, verbose_name='文件名')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file', to='tree.Node')),
            ],
        ),
    ]