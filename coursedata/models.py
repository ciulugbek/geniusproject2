from django.db import models
from django.db.models import UniqueConstraint
from PIL import Image

# Create your models here.
class Groups(models.Model):
    group_name=models.CharField(max_length=100, unique=True)
    group_create_date=models.DateField(auto_now=True)
    group_active=models.BooleanField(default=True)

def __str__(self):
    return f"{self.group_name} {self.group_create_date} is {self.group_active}"


class Student(models.Model):
    student_fio=models.CharField(max_length=150)
    student_create_date=models.DateField(auto_now=True)
    student_active=models.BooleanField(default=True)
    student_phone=models.CharField(max_length=60, unique=True)
    student_email=models.EmailField(max_length = 100)
    student_photo=models.ImageField(upload_to='student_images/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.student_photo:
           img1 = Image.open(self.student_photo.path)
           if img1.height > 1500 or img1.width > 1500:
              output_size = (1500, 1500)
              img1.thumbnail(output_size)
              img1.save(self.student_photo.path)

    def __str__(self):
        return f"{self.student_fio} {self.student_create_date} {self.student_phone} is {self.student_active}"

class Parent(models.Model):
    parent_fio=models.CharField(max_length=150)
    parent_active=models.BooleanField(default=True)
    parent_phone=models.CharField(max_length=60, unique=True)

def __str__(self):
    return f"{self.parent_fio} {self.parent_phone} is {self.parent_active}"


    
class StudentParent(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE)
    student_parent_active=models.BooleanField(default=True)

    
    # unique_together = ('student_id', 'parent_id',)
    class Meta:
        constraints = [
            UniqueConstraint('student_id','parent_id',name='student_parent_unique',),
        ]

class StudentGroup(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE)
    student_group_active=models.BooleanField(default=True)

    
    # unique_together = ('student_id', 'group_id',)
    class Meta:
        constraints = [
            UniqueConstraint('student_id','group_id',name='student_group_unique',),
        ]        

