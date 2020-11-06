# Generated by Django 3.1 on 2020-10-08 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_con',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Message', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('typ', models.CharField(default='teacher', max_length=50)),
            ],
        ),
    ]