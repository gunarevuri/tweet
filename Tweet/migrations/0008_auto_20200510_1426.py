# Generated by Django 3.0.2 on 2020-05-10 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tweet', '0007_auto_20200510_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='Total',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='hostel',
            name='Total',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='professor',
            name='Total',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='dept_ratings',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='ratings',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='professor',
            name='p_ratings',
            field=models.IntegerField(null=True),
        ),
    ]
