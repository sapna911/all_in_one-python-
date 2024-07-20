from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    gender_choice=(
        ('Male','Male'),
        ('female','female')
    )
    gender=models.CharField(max_length=7,choices=gender_choice)



    class Meta:
        db_table="student_info"