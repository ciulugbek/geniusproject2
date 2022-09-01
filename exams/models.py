from django.db import models
from django.db.models import UniqueConstraint
from coursedata.models import Groups,Student, StudentGroup
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Exam(models.Model):
    exam_name=models.CharField(max_length=100, unique=True)

class ExamGroup(models.Model):
    exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)
    group_id=models.ForeignKey(Groups, on_delete=models.CASCADE)
    exam_group_date=models.DateField()

    class Meta:
        constraints = [
            UniqueConstraint('exam_id','group_id','exam_group_date',name='exam_group_date_unique',),
        ]

class ExamStudent(models.Model):
    exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student_group_id=models.ForeignKey(StudentGroup, on_delete=models.CASCADE)
    exam_student_date=models.DateField()

    class Meta:
        constraints = [
            UniqueConstraint('exam_id','student_group_id','exam_student_date',name='exam_student_date_unique',),
        ]

class ExamGroupResult(models.Model):
    exam_group_id = models.ForeignKey(ExamGroup, on_delete=models.CASCADE)
    student_group_id=models.ForeignKey(StudentGroup, on_delete=models.CASCADE)
    exam_percent=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    exam_comment=models.CharField(max_length=255)
    class Meta:
        constraints = [
            UniqueConstraint('exam_group_id','student_group_id',name='exam_group_result_unique',),
        ]


# class ExamStudentResult(models.Model):
#     exam_student_id = models.ForeignKey(ExamStudent, on_delete=models.CASCADE)
#     # student_group_id=models.ForeignKey(StudentGroup, on_delete=models.CASCADE)
#     exam_percent=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
#     exam_comment=models.CharField(max_length=255)

#     class Meta:
#         constraints = [
#             UniqueConstraint('exam_student_id',name='exam_student_result_unique',),
#         ]
    
class ExamStudentResult(models.Model):
    exam_student_id = models.OneToOneField(ExamStudent, on_delete=models.CASCADE,primary_key=True)
    exam_percent=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    exam_comment=models.CharField(max_length=255)

    class Meta:
        constraints = [
            UniqueConstraint('exam_student_id',name='exam_student_result_unique',),
        ]