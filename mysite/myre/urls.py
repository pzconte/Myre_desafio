from django.urls import path

from . import views

app_name = 'myre'

urlpatterns = [
    path('', views.index, name='index'),
    path('projects', views.project_list, name='project_list'),
    path('schools', views.school_list, name='school_list'),
    path('<int:school_id>/students/', views.students_list, name='students_list'),
    path('<int:school_id>/grades/', views.grades_list, name='grade_list'),
    path('add_school', views.add_school, name='add_school'),
    path('add_project', views.add_project, name='add_project'),
    path('add_grade', views.add_grade, name='add_grade'),
    path('add_student', views.add_student, name='add_student'),
]