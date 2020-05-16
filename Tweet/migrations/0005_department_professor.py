# Generated by Django 3.0.2 on 2020-05-10 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tweet', '0004_auto_20190312_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart_name', models.CharField(max_length=50)),
                ('dept_code', models.CharField(max_length=10)),
                ('dept_ratings', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professor_name', models.CharField(max_length=30)),
                ('p_id', models.CharField(max_length=10)),
                ('number', models.CharField(max_length=10)),
                ('p_ratings', models.IntegerField()),
                ('dept_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tweet.Department')),
            ],
        ),
    ]
