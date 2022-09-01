# Generated by Django 4.1 on 2022-08-30 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examstudentresult',
            name='id',
        ),
        migrations.AlterField(
            model_name='examstudentresult',
            name='exam_student_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='exams.examstudent'),
        ),
    ]
