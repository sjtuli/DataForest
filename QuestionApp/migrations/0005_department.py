# Generated by Django 3.2.8 on 2021-10-22 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionApp', '0004_question_users_unlike'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='名称')),
                ('parent', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='QuestionApp.department', verbose_name='父部门')),
            ],
        ),
    ]
