from django.db import models

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=200, unique=True)
    project_date = models.DateField('date started')

    def __str__(self):
        return f"{self.id} {self.project_name}"

class School(models.Model):
    school_name = models.CharField(max_length=200, unique=True, null=False, blank=False)

    def __str__(self):
        return f"{self.school_name}"
    
class Project_data(models.Model):
    # if a Project is deleted then all Project_data must be deleted then on_delete must be CASCADE
    id_project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="School")
    # if a School is deleted then all of the projects must be deleted then on_delete must be CASCADE
    id_school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="Project")
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_project', 'id_school'], name='unique school on a proyect')
        ]

class Grade(models.Model):
    year = models.IntegerField()
    # if a School is deleted then all Grades must be deleted then on_delete must be CASCADE
    id_school = models.ForeignKey(School, on_delete=models.CASCADE)
    class Level(models.TextChoices):
        FIRST_GRADE = '1', '1 basico'
        SECOND_GRADE = '2', '2 basico'
        THIRD_GRADE = '3', '3 basico'
        FOURTH_GRADE = '4', '4 basico'
    level = models.CharField(
        max_length=1,
        choices=Level.choices,
        default=Level.FIRST_GRADE
    )
    class Section(models.TextChoices):
        A = 'A', 'Sección A'
        B = 'B', 'Sección B'
        C = 'C', 'Sección C'
        D = 'D', 'Sección D'
    section = models.CharField(
        max_length=1,
        choices=Section.choices,
        default=Section.A
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['year', 'level', 'section','id_school'], name='unique grade on a year')
        ]
    def __str__(self):
        return f"{self.level} {self.section} {self.year} - {self.id_school}"
    
class Student(models.Model):
    student_fullname = models.CharField(max_length=200)
    rut = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return f"{self.rut} {self.student_fullname}"

class Student_grade(models.Model):
    # if a Student is deleted then all of the Students_grade must be deleted then on_delete must be CASCADE
    id_student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='Grade')
    # if a Grade is deleted then all of the Students_grade must be deleted then on_delete must be CASCADE
    id_grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='Student')
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_student', 'id_grade'], name='unique student on a grade')
        ]

    def __str__(self):
        return f"{self.id_grade} - {self.id_student}"