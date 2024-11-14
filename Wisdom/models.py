from django.db import models
from datetime import date


# Create your models here.
class Course(models.Model):
    COURSE_CHOICES = (
        (1, 'C'),
        (2, 'C++'),
        (3, 'JAVA'),
        (4, 'PYTHON'),
        (5, 'DATA SCIENCE'),
        (6, 'MACHINE LEARNING'),
    )
    name = models.IntegerField(choices=COURSE_CHOICES)
    description = models.TextField()
    credits = models.IntegerField()

    def __str__(self):
        return self.get_name_display()


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=300)
    courses = models.ManyToManyField(Course, through='Enrollment')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Faculty(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.student} enrolled in {self.course} on {self.enrollment_date}"
