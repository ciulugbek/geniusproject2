from django.urls import path
from .views import (HomeView, GroupListView, GroupCreateView, GroupUpdateView, GroupDeleteView,
                    StudentDeleteView,
                    ParentListView, ParentCreateView, ParentUpdateView, ParentDeleteView, 
                    StudentParentList, StudentParentAdd, StudentParentDeleteView, StudentParentUpdate,
                    StudentGroupList, StudentGroupAdd, StudentGroupDeleteView, StudentGroupUpdate,
                    create_student_view,create_student_success,update_student_view, update_student_success, student_list)
# StudentListView, StudentCreateView, StudentUpdateView,
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

app_name='coursedata'

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='home_coursedata'),
    path('group_list/', login_required(GroupListView.as_view()), name='group_list'),
    path('create_group/',login_required(GroupCreateView.as_view()),name='create_group'),
    path('group_update/<int:pk>',login_required(GroupUpdateView.as_view()),name='group_update'),
    path('group_delete/<int:pk>',login_required(GroupDeleteView.as_view()),name='group_delete'),
    # path('student_list/', StudentListView.as_view(), name='student_list'),
    path('student_list/', login_required(student_list), name='student_list'),
    # path('create_student/',StudentCreateView.as_view(),name='create_student'),
    path('create_student/',login_required(create_student_view),name='create_student'),
    path('create_student_success/', login_required(create_student_success), name = 'create_student_success'),
    # path('student_update/<int:pk>',StudentUpdateView.as_view(),name='student_update'),
    path('student_update/<int:pk>',login_required(update_student_view),name='student_update'),
    path('update_student_success/', login_required(update_student_success), name = 'update_student_success'),
    path('student_delete/<int:pk>',login_required(StudentDeleteView.as_view()),name='student_delete'),
    path('parent_list/', login_required(ParentListView.as_view()), name='parent_list'),
    path('create_parent/',login_required(ParentCreateView.as_view()),name='create_parent'),
    path('parent_update/<int:pk>',login_required(ParentUpdateView.as_view()),name='parent_update'),
    path('parent_delete/<int:pk>',login_required(ParentDeleteView.as_view()),name='parent_delete'),
    path('student_parent_list/', login_required(StudentParentList), name='student_parent_list'),
    path('creare_student_parent/', login_required(StudentParentAdd), name='create_student_parent'),
    path('student_parent_delete/<int:pk>',login_required(StudentParentDeleteView.as_view()),name='student_parent_delete'),
    path('student_parent_update/<int:pk>',login_required(StudentParentUpdate),name='student_parent_update'),
    path('student_group_list/', login_required(StudentGroupList), name='student_group_list'),
    path('creare_student_group/', login_required(StudentGroupAdd), name='create_student_group'),
    path('student_group_delete/<int:pk>',login_required(StudentGroupDeleteView.as_view()),name='student_group_delete'),
    path('student_group_update/<int:pk>',login_required(StudentGroupUpdate),name='student_group_update'),
    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)