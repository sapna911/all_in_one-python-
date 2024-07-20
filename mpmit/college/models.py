from django.db import models
from django.db import models

# Create your models here.
'''
class CourseDetail:

    name:str
    img:str
    price:str
    offer:bool
'''
class CourseDetail(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    price=models.IntegerField()
    offer=models.BooleanField(default=False)