from django.shortcuts import render
from .models import CourseDetail
# Create your views here.
'''

s1 = CourseDetail()
s1.name = 'Django python'
s1.price = '600'
s1.offer=False

s2 = CourseDetail()
s2.name = 'JAVA'
s2.price = '40000'
s2.offer=True


s3 = CourseDetail()
s3.name = 'php'
s3.price = '60000'
s3.offer=False




ob = [s1, s2, s3, ]


def index(request):
    return render(request,'index.html',{'object':ob})
'''
def index(request):
    ob=CourseDetail.objects.all()
    return render(request, 'index.html', {'object': ob})
