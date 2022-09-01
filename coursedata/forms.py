from django import forms
from .models import *
# from django.forms import ModelForm

class CreateGroupForm(forms.Form):
    group_name=forms.CharField(max_length=50)
    # group_create_date=forms.DateField(auto_now=True)
    group_active=forms.BooleanField()
    
class CreateStudentForm(forms.Form):
    student_fio=forms.CharField(max_length=150)
    # student_create_date=forms.DateField(auto_now=True)
    student_active=forms.BooleanField()
    student_phone=forms.CharField(max_length=60)
    student_email=forms.EmailField(max_length = 100)
    student_photo=forms.ImageField()

    

class CreateParentForm(forms.Form):
    parent_fio=forms.CharField(max_length=150)
    parent_active=forms.BooleanField()
    parent_phone=forms.CharField(max_length=60)


class CreateStudentForm2(forms.ModelForm):
  
    class Meta:
        model = Student
        fields = ['student_fio', 'student_active','student_phone','student_email','student_photo']

    