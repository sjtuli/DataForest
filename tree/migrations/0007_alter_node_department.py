# Generated by Django 3.2.8 on 2021-10-25 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0006_auto_20211024_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depart', to='tree.department', verbose_name='节点'),
        ),
    ]
