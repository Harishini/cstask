from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    if request.method=='POST':
        week=request.POST.get('week')
        cname=request.POST.get('course_name')
        resource_person=request.POST.get('resource_person')

        newcourse=course(week=week,course_name=cname,resource_person=resource_person)
        newcourse.save()
        return render(request,'list/courseadded.html')
    return render(request,'list/index.html')


def courseadded(request):
    return render(request,'list/courseadded.html')
def check(request):
    detail=course.objects.all()
    return render(request,'list/check.html',{'detail':detail})
