from django import forms
from .models import Project, Project_data, School, Student, Grade, Student_grade


class SchoolForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = School

        # specify fields to be used
        fields = [
            "school_name",
        ]

class ProjectForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Project
        # specify fields to be used
        fields = [
            "project_name", "project_date",
        ]

class GradeForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Grade

        # specify fields to be used
        fields = [
            "level", "section", "year", "id_school",
        ]

class StudentForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Student
        # specify fields to be used
        fields = [
            "student_fullname", "rut",
        ]

class Student_gradeForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Student_grade
        # specify fields to be used
        fields = [
            "id_grade",
        ]
