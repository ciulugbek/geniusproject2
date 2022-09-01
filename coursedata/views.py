from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import *
from .models import Groups, Student, Parent, StudentParent, StudentGroup
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.

# @login_required
def home_view(request):
    return render(request,'coursedata/home.html')

# @login_required
class HomeView(TemplateView):
    template_name='coursedata/home.html'

# @login_required    
class GroupCreateView(CreateView):
    model=Groups
    fields="__all__"
    success_url=reverse_lazy('coursedata:group_list')

# @login_required
class GroupListView(ListView):
    model=Groups
    # queryset=Teacher.objects.all()
    queryset=Groups.objects.order_by('group_name')
    context_object_list="groups_list"

# @login_required
class GroupUpdateView(UpdateView):
    model=Groups
    fields=['group_name','group_active']
    success_url=reverse_lazy('coursedata:group_list')

# @login_required
class GroupDeleteView(DeleteView):
    model=Groups
    success_url=reverse_lazy('coursedata:group_list')

# @login_required
def create_student_view(request):
  
    if request.method == 'POST':
        form = CreateStudentForm2(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('coursedata:create_student_success')
    else:
        form = CreateStudentForm2()
    return render(request, 'coursedata/student_form2.html', {'form' : form})
  

# @login_required  
def create_student_success(request):
    # return HttpResponse('successfully uploaded')
    return render(request, 'coursedata/student_form2_success.html')

# class StudentCreateView(CreateView):
#     model=Student
#     fields="__all__"
#     success_url=reverse_lazy('coursedata:student_list')


# @login_required
def student_list(request):
    # list_student=Student.objects.all().order_by('id')
    p = Paginator(Student.objects.all(),2)
    page = request.GET.get('page')
    list_student = p.get_page(page)
    nums="a"*list_student.paginator.num_pages
    # return HttpResponse('successfully uploaded')
    return render(request, 'coursedata/student_list2.html', {'list_student':list_student,'nums':nums})

# class StudentListView(ListView):
#     model=Student
#     # queryset=Teacher.objects.all()
#     queryset=Student.objects.order_by('student_fio')
    
#     context_object_list="student_list"

# @login_required
def update_student_view(request,pk):
  
    if request.method == 'POST':
    #     form = CreateStudentForm2(request.POST, request.FILES)
  
    #     if form.is_valid():
    #         form.save()
    #         return redirect('coursedata:update_student_success')
        student_fio=request.POST['student_fio']
        if 'student_active' not in request.POST:
            student_active_kod = False
        else:
            if request.POST['student_active']=="checked":
                student_active_kod=True
            else:
                student_active_kod=False

        student_phone=request.POST['student_phone']
        student_email=request.POST['student_email']
        # student_photo=request.POST['student_photo']
        student_photo = request.FILES.get('student_photo')
        student_cur_obj=Student.objects.get(pk=pk)
       
        student_cur_obj.student_fio=student_fio
        student_cur_obj.student_active=student_active_kod
        student_cur_obj.student_phone=student_phone
        student_cur_obj.student_email=student_email
        student_cur_obj.student_photo=student_photo
        # student_cur_obj.student_photo=student_photo
        # student_photo = request.FILES.get('student_photo')
        student_cur_obj.save()
        # StudentParent.objects.create(student_id=student,parent_id=parent,student_parent_active=student_parent_active_kod)
        return redirect(reverse('coursedata:student_list'))

    else:
        student_obj=Student.objects.get(pk=pk) 
        context={'student_obj':student_obj}
        return render(request,'coursedata/student_update_form2.html',context=context)

    #     form = CreateStudentForm2(request)
    # return render(request, 'coursedata/student_update_form2.html', {'form' : form})
  
  
# @login_required  
def update_student_success(request):
    # return HttpResponse('successfully uploaded')
    return render(request, 'coursedata/student_update_form2_success.html')

# class StudentUpdateView(UpdateView):
#     model=Student
#     fields=['student_fio','student_active','student_phone']
    success_url=reverse_lazy('coursedata:student_list')

# @login_required
class StudentDeleteView(DeleteView):
    model=Student
    success_url=reverse_lazy('coursedata:student_list')

# @login_required
class ParentCreateView(CreateView):
    model=Parent
    fields="__all__"
    success_url=reverse_lazy('coursedata:parent_list')

# @login_required
class ParentListView(ListView):
    model=Parent
    # queryset=Teacher.objects.all()
    queryset=Parent.objects.order_by('parent_fio')
    context_object_list="parent_list"


# @login_required
class ParentUpdateView(UpdateView):
    model=Parent
    fields=['parent_fio','parent_active','parent_phone']
    success_url=reverse_lazy('coursedata:parent_list')

# @login_required
class ParentDeleteView(DeleteView):
    model=Parent
    success_url=reverse_lazy('coursedata:parent_list')

# @login_required
def StudentParentList(request):
    studentparent_obj=StudentParent.objects.all()
    
    # print(studentparent_obj.student_id.id) 
    
    context={'studentparent_obj':studentparent_obj}
    return render(request,'coursedata/student_parent_list.html',context=context)

# @login_required
def StudentParentAdd(request):
    if request.POST:
        student_kod=request.POST['student']
        student=Student.objects.get(pk=student_kod)
        parent_kod=request.POST['parent']
        parent=Parent.objects.get(pk=parent_kod)
        
        if 'student_parent_active' not in request.POST:
            student_parent_active_kod = False
        else:
            if request.POST['student_parent_active']=="checked":
                student_parent_active_kod=True
            else:
                student_parent_active_kod=False
        # print(student_parent_active_kod)
    #        student_parent_active_kod = request.POST['student_parent_active']
        
        StudentParent.objects.create(student_id=student,parent_id=parent,student_parent_active=student_parent_active_kod)
        return redirect(reverse('coursedata:student_parent_list'))
    else:
        student_obj=Student.objects.all() 
        parent_obj=Parent.objects.all() 
        # context1={'student_obj':student_obj}
        # context2={'parent_obj':parent_obj}
        return render(request,'coursedata/student_parent_add.html',{"student_obj":student_obj,"parent_obj":parent_obj})

# @login_required
class StudentParentDeleteView(DeleteView):
    model=StudentParent
    success_url=reverse_lazy('coursedata:student_parent_list')

# @login_required
def StudentParentUpdate(request, pk):
    if request.POST:
        student_kod=request.POST['student']
        student=Student.objects.get(pk=student_kod)
        parent_kod=request.POST['parent']
        parent=Parent.objects.get(pk=parent_kod)
        
        if 'student_parent_active' not in request.POST:
            student_parent_active_kod = False
        else:
            if request.POST['student_parent_active']=="checked":
                student_parent_active_kod=True
            else:
                student_parent_active_kod=False

        
        student_parent_cur_obj=StudentParent.objects.get(pk=pk)
       
        # student_parent_cur_obj.refresh_from_db()
        student_parent_cur_obj.student_id=student
        student_parent_cur_obj.parent_id=parent
        student_parent_cur_obj.student_parent_active=student_parent_active_kod 
        student_parent_cur_obj.save()
        # StudentParent.objects.create(student_id=student,parent_id=parent,student_parent_active=student_parent_active_kod)
        return redirect(reverse('coursedata:student_parent_list'))
        # return HttpResponse("asa")
    else:
        student_obj=Student.objects.all() 
        parent_obj=Parent.objects.all()
        student_parent_cur_obj=StudentParent.objects.get(pk=pk)
        print(student_parent_cur_obj.student_parent_active)
        # return HttpResponse('asd')
        return render(request,'coursedata/student_parent_update.html', {"student_obj":student_obj,"parent_obj":parent_obj,'student_parent_cur_obj':student_parent_cur_obj})


# @login_required
def StudentGroupList(request):
    studentgroup_obj=StudentGroup.objects.all()
    
    # print(studentparent_obj.student_id.id) 
    
    context={'studentgroup_obj':studentgroup_obj}
    return render(request,'coursedata/student_group_list.html',context=context)

# @login_required
def StudentGroupAdd(request):
    if request.POST:
        student_kod=request.POST['student']
        student=Student.objects.get(pk=student_kod)
        group_kod=request.POST['group']
        group=Groups.objects.get(pk=group_kod)
        
        if 'student_group_active' not in request.POST:
            student_group_active_kod = False
        else:
            if request.POST['student_group_active']=="checked":
                student_group_active_kod=True
            else:
                student_group_active_kod=False
        # print(student_parent_active_kod)
    #        student_parent_active_kod = request.POST['student_parent_active']
        
        StudentGroup.objects.create(student_id=student,group_id=group,student_group_active=student_group_active_kod)
        return redirect(reverse('coursedata:student_group_list'))
    else:
        student_obj=Student.objects.all() 
        group_obj=Groups.objects.all() 
        # context1={'student_obj':student_obj}
        # context2={'parent_obj':parent_obj}
        return render(request,'coursedata/student_group_add.html',{"student_obj":student_obj,"group_obj":group_obj})

# @login_required
class StudentGroupDeleteView(DeleteView):
    model=StudentGroup
    success_url=reverse_lazy('coursedata:student_group_list')

# @login_required
def StudentGroupUpdate(request, pk):
    if request.POST:
        student_kod=request.POST['student']
        student=Student.objects.get(pk=student_kod)
        group_kod=request.POST['group']
        group=Groups.objects.get(pk=group_kod)
        
        if 'student_group_active' not in request.POST:
            student_group_active_kod = False
        else:
            if request.POST['student_group_active']=="checked":
                student_group_active_kod=True
            else:
                student_group_active_kod=False

        
        student_group_cur_obj=StudentGroup.objects.get(pk=pk)
       
        # student_parent_cur_obj.refresh_from_db()
        student_group_cur_obj.student_id=student
        student_group_cur_obj.group_id=group
        student_group_cur_obj.student_group_active=student_group_active_kod 
        student_group_cur_obj.save()
        # StudentParent.objects.create(student_id=student,parent_id=parent,student_parent_active=student_parent_active_kod)
        return redirect(reverse('coursedata:student_group_list'))
        # return HttpResponse("asa")
    else:
        student_obj=Student.objects.all() 
        group_obj=Groups.objects.all()
        student_group_cur_obj=StudentGroup.objects.get(pk=pk)
        # print(student_group_cur_obj.student_group_active)
        # return HttpResponse('asd')
        return render(request,'coursedata/student_group_update.html', {"student_obj":student_obj,"group_obj":group_obj,'student_group_cur_obj':student_group_cur_obj})

