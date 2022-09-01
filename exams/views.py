from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Exam, ExamGroup,ExamStudent,ExamStudentResult, ExamGroupResult
from coursedata.models  import Groups, Student,StudentGroup
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return render(request,'exams/home.html')

class HomeView(TemplateView):
    template_name='exams/home.html'

class ExamListView(ListView):
    model=Exam
    queryset=Exam.objects.order_by('exam_name')
    context_object_list="exam_list"

class ExamCreateView(CreateView):
    model=Exam
    fields="__all__"
    success_url=reverse_lazy('exams:exam_list')

class ExamUpdateView(UpdateView):
    model=Exam
    fields=['exam_name']
    success_url=reverse_lazy('exams:exam_list')

class ExamDeleteView(DeleteView):
    model=Exam
    success_url=reverse_lazy('exams:exam_list')

def ExamGroupList(request):
    examgroup_obj=ExamGroup.objects.all()
    context={'examgroup_obj':examgroup_obj}
    return render(request,'exams/exam_group_list.html',context=context)

def ExamGroupAdd(request):
    if request.POST:
        exam_kod=request.POST['exam']
        exam=Exam.objects.get(pk=exam_kod)
        group_kod=request.POST['group']
        group=Groups.objects.get(pk=group_kod)
        exam_group_date=request.POST['exam_group_date']
        ExamGroup.objects.create(exam_id=exam,group_id=group,exam_group_date=exam_group_date)
        return redirect(reverse('exams:exam_group_list'))
    else:
        exam_obj=Exam.objects.all() 
        group_obj=Groups.objects.all() 
        return render(request,'exams/exam_group_add.html',{"exam_obj":exam_obj,"group_obj":group_obj})

class ExamGroupDeleteView(DeleteView):
    model=ExamGroup
    success_url=reverse_lazy('exams:exam_group_list')

def ExamGroupUpdate(request, pk):
    if request.POST:
        exam_kod=request.POST['exam']
        exam=Exam.objects.get(pk=exam_kod)
        group_kod=request.POST['group']
        group=Groups.objects.get(pk=group_kod)
        exam_group_date=request.POST['exam_group_date']
        exam_group_cur_obj=ExamGroup.objects.get(pk=pk)
        exam_group_cur_obj.exam_id=exam
        exam_group_cur_obj.group_id=group
        exam_group_cur_obj.exam_group_date=exam_group_date 
        exam_group_cur_obj.save()
        return redirect(reverse('exams:exam_group_list'))
    else:
        exam_obj=Exam.objects.all() 
        group_obj=Groups.objects.all()
        exam_group_cur_obj=ExamGroup.objects.get(pk=pk)
        return render(request,'exams/exam_group_update.html', {"exam_obj":exam_obj,"group_obj":group_obj,'exam_group_cur_obj':exam_group_cur_obj})


def ExamStudentList(request):
    examstudent_obj=ExamStudent.objects.all()
    context={'examstudent_obj':examstudent_obj}
    return render(request,'exams/exam_student_list.html',context=context)

def ExamStudentAdd(request):
    if request.POST:
        exam_kod=request.POST['exam']
        exam=Exam.objects.get(pk=exam_kod)
        group_kod=request.POST['group']
        student_kod=request.POST['student']
        exam_student_date=request.POST['exam_student_date']
        student_group_id=StudentGroup.objects.filter(student_id=student_kod,group_id=group_kod).first()
        ExamStudent.objects.create(exam_id=exam,student_group_id=student_group_id,exam_student_date=exam_student_date)
        return redirect(reverse('exams:exam_student_list'))
    else:
        exam_obj=Exam.objects.all()
        group_obj=Groups.objects.all()  
        student_obj=Student.objects.all() 
        return render(request,'exams/exam_student_add.html',{"exam_obj":exam_obj,"group_obj":group_obj,"student_obj":student_obj})

class ExamStudentDeleteView(DeleteView):
    model=ExamStudent
    success_url=reverse_lazy('exams:exam_student_list')

def ExamStudentUpdate(request, pk):
    if request.POST:
        exam_kod=request.POST['exam']
        exam=Exam.objects.get(pk=exam_kod)
        group_kod=request.POST['group']
        student_kod=request.POST['student']
        exam_student_date=request.POST['exam_student_date']
        exam_student_cur_obj=ExamStudent.objects.get(pk=pk)
        student_group_id=StudentGroup.objects.filter(student_id=student_kod,group_id=group_kod).first()
        exam_student_cur_obj.exam_id=exam
        exam_student_cur_obj.student_group_id=student_group_id
        exam_student_cur_obj.exam_student_date=exam_student_date 
        exam_student_cur_obj.save()
        return redirect(reverse('exams:exam_student_list'))

    else:
        exam_obj=Exam.objects.all() 
        group_obj=Groups.objects.all()
        student_obj=Student.objects.all()
        exam_student_cur_obj=ExamStudent.objects.get(pk=pk)
        
        return render(request,'exams/exam_student_update.html', {"exam_obj":exam_obj,"group_obj":group_obj,"student_obj":student_obj,'exam_student_cur_obj':exam_student_cur_obj})


def ExamStudentResultList(request):
    examstudentresult_obj=ExamStudentResult.objects.all()
    context={'examstudentresult_obj':examstudentresult_obj}
    return render(request,'exams/exam_student_result_list.html',context=context)


def ExamStudentResultInd(request, pk):
    ExamStudentResultInd_obj=ExamStudentResult.objects.filter(exam_student_id=pk).first()
    
    if not ExamStudentResultInd_obj:
        return redirect(reverse('exams:create_exam_student_result_ind',args=(pk,)))
    
    else:
        pk=ExamStudentResultInd_obj.exam_student_id.id
        return redirect(reverse('exams:exam_student_result_ind_update',args=(pk,)))
    

def ExamStudentResultIndUpdate(request, pk):
    if request.POST:
        exam_student_kod=request.POST['exam_student']
        exam_student_id=ExamStudent.objects.get(pk=exam_student_kod)
        exam_percent=request.POST['exam_percent']
        exam_comment=request.POST['exam_student_result_comment']
        exam_student_result_cur_obj=ExamStudentResult.objects.get(pk=pk)
        exam_student_result_cur_obj.exam_percent=exam_percent
        exam_student_result_cur_obj.exam_percentexam_comment=exam_comment
        exam_student_result_cur_obj.save()
        return redirect(reverse('exams:exam_student_list'))
    else:
        ExamStudentResultInd_obj=ExamStudentResult.objects.get(pk=pk)
        return render(request,'exams/exam_student_result_ind_update.html', {"ExamStudentResultInd_obj":ExamStudentResultInd_obj})

def ExamStudentResultAddInd(request,pk):
    if request.POST:
        exam_student_kod=request.POST['exam_student']
        exam_percent=request.POST['exam_percent']
        exam_comment=request.POST['exam_student_result_comment']
        exam_student_id=ExamStudent.objects.get(pk=exam_student_kod)
        ExamStudentResult.objects.create(exam_student_id=exam_student_id,exam_percent=exam_percent,exam_comment=exam_comment)
        return redirect(reverse('exams:exam_student_list'))
        
    else:
        examstudent_cur_obj=ExamStudent.objects.get(pk=pk)
        return render(request,'exams/exam_student_result_ind_add.html',{"examstudent_cur_obj":examstudent_cur_obj})
        

def ExamGroupResultList(request):
    examgroupresult_obj=ExamGroupResult.objects.all()
    context={'examgroupresult_obj':examgroupresult_obj}
    return render(request,'exams/exam_group_result_list.html',context=context)

def ExamGroupResultView(request, pk):
    # ExamStudentResultInd_obj=ExamStudentResult.objects.filter(exam_student_id=pk).first()
    # if not ExamStudentResultInd_obj:
    #     return redirect(reverse('exams:create_exam_student_result_ind',args=(pk,)))
    # else:
    #     pk=ExamStudentResultInd_obj.exam_student_id.id
    return redirect(reverse('exams:create_exam_group_result',args=(pk,)))

def ExamGroupResultAdd(request, pk):
    examgroup_cur_obj=ExamGroup.objects.get(pk=pk)
    studentgroup_obj = StudentGroup.objects.filter(group_id=examgroup_cur_obj.group_id.id).all()
    examgroupresult_cur_obj=ExamGroupResult.objects.filter(exam_group_id=examgroup_cur_obj.id).all()
    if not examgroupresult_cur_obj:
        return render(request,'exams/exam_group_result_list_add.html',{"examgroup_cur_obj":examgroup_cur_obj,
                                                                    "studentgroup_obj":studentgroup_obj,
                                                                    "vhasresult":False})

    else:
        return render(request,'exams/exam_group_result_list_add.html',{"examgroup_cur_obj":examgroup_cur_obj,
                                                                    "examgroupresult_cur_obj":examgroupresult_cur_obj,
                                                                    "studentgroup_obj":studentgroup_obj,
                                                                    "vhasresult":True})

def ExamGroupStudentResultAddInd(request,egpk,sgpk):
        ExamGroupResultInd_obj=ExamGroupResult.objects.filter(exam_group_id=egpk,student_group_id=sgpk).first()
        if not ExamGroupResultInd_obj:
            return redirect(reverse('exams:create_exam_group_student_result_ind2',args=(egpk,sgpk)))
    
        else:
            pk=ExamStudentResultInd_obj.exam_student_id.id
            return redirect(reverse('exams:exam_student_result_ind_update2',args=(egpk,sgpk)))
        

def ExamGroupStudentResultAddInd2(request,egpk,sgpk):
    if request.POST:
        exam_group_student_kod=request.POST['exam_group_student']
        exam_group=ExamGroup.objects.get(pk=exam_group_student_kod)
        student_group_kod=request.POST['student_group']
        student_group=StudentGroup.objects.get(pk=student_group_kod)
        exam_percent=request.POST['exam_percent']
        exam_comment=request.POST['exam_group_student_result_comment']
        # exam_student_id=ExamStudent.objects.get(pk=exam_student_kod)
        ExamGroupResult.objects.create(exam_group_id=exam_group,student_group_id=student_group,exam_percent=exam_percent,exam_comment=exam_comment)
        # return redirect(reverse('exams:exam_group_result_list',args=(egpk,sgpk)))
        pk=exam_group_student_kod
        return redirect(reverse('exams:create_exam_group_result',args=(pk,)))
        
    else:
        examgroup_cur_obj=ExamGroup.objects.get(pk=egpk)
        studentgroup_obj = StudentGroup.objects.get(pk=sgpk)
        # ExamGroupResultInd_obj=ExamGroupResult.objects.filter(exam_group_id=egpk,student_group_id=sgpk).first()
        return render(request,'exams/exam_group_student_result_ind_add.html',{"examgroup_cur_obj":examgroup_cur_obj,"studentgroup_obj":studentgroup_obj})                                                                            