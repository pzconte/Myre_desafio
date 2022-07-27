from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .forms import SchoolForm, ProjectForm, GradeForm, StudentForm, Student_gradeForm

from .models import Project, Project_data, School, Student, Grade, Student_grade


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the myre index.")

def project_list(request):
    all_projects = Project.objects.order_by('project_name')
    template = loader.get_template('myre/projects.html')
    context = {
        'all_projects': all_projects,
    }
    return HttpResponse(template.render(context, request))

def school_list(request):
    all_schools = School.objects.order_by('school_name')
    template = loader.get_template('myre/schools.html')
    context = {
        'all_schools': all_schools,
    }
    return HttpResponse(template.render(context, request))

def students_list(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    all_students = Student.objects.order_by('student_fullname')
    template = loader.get_template('myre/students.html')
    context = {
        'all_students': all_students,
        'school': school,
    }
    return HttpResponse(template.render(context, request))
    
def grades_list(request, school_id):
    school_grade = get_object_or_404(School, pk=school_id)
    all_grades = Grade.objects.order_by('year')
    template = loader.get_template('myre/grades.html')
    context = {
        'all_grades': all_grades,
        'school_grade': school_grade,
    }
    return HttpResponse(template.render(context, request))

def add_school(request):
    template = loader.get_template('myre/add_school.html')
    context = {}
    form = SchoolForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return HttpResponse(template.render(context, request))

def add_project(request):
    template = loader.get_template('myre/add_project.html')
    context = {}
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return HttpResponse(template.render(context, request))

def add_grade(request):
    template = loader.get_template('myre/add_grade.html')
    context = {}
    form = GradeForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return HttpResponse(template.render(context, request))

def add_student(request):
    template = loader.get_template('myre/add_student.html')
    context = {}
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return HttpResponse(template.render(context, request))
