from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name



class Faculty(models.Model):
    name = models.CharField(max_length=300)

class Department(models.Model):
    name = models.CharField(max_length=400)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

class Certificate_type(models.Model):
    name = models.CharField(max_length=100)

class Grade(models.Model):
    type = models.CharField(max_length=4)

class Student(models.Model):
    fullname = models.CharField(max_length=40)
    year_of_graduation = models.DateTimeField(default=datetime.today)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(Certificate_type, on_delete=models.CASCADE)
