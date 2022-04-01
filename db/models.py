from django.db import models
from manage import init_django

init_django()


SEMESTER_CHOICES = (
    (1, "FIRST"),
    (2, "SECOND"),
)


class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    reg_number = models.CharField(max_length=12, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    other_names = models.CharField(max_length=255, null=True, blank=True)
    level_of_study = models.IntegerField(null=True, blank=True)
    fingerprint_template = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.reg_number})"

class Course(models.Model):


    class SemesterList(models.IntegerChoices):
        FIRST = 1
        SECOND = 2


    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=8)
    title = models.CharField(max_length=255)
    unit_load = models.IntegerField()
    semester = models.IntegerField(SemesterList.choices)
    elective = models.BooleanField(default=False)


class Session(models.Model):
    id = models.BigAutoField(primary_key=True)
    session = models.CharField(max_length=10)
    description = models.CharField(max_length=255)


class Attendance(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    sign_in = models.DateTimeField(auto_now=True)
    # exam = models.BooleanField(default=False)