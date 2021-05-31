from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone


# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name



class Faculty(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=400)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Certificate_type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Grade(models.Model):
    type = models.CharField(max_length=4)

    def __str__(self):
        return self.type

class Student(models.Model):
    fullname = models.CharField(max_length=40)
    year_of_graduation = models.DateTimeField(default=timezone.now)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(Certificate_type, on_delete=models.CASCADE)


    def __str__(self):
        return self.fullname
