# Generated by Django 4.1 on 2022-08-06 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursedata', '0006_rename_parent_studentparent_parent_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='parent_phone',
            field=models.CharField(max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_phone',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
