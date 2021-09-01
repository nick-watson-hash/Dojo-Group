from django.shortcuts import render, redirect
from django.contrib import messages
from courses_app.models import *

# Create your views here.
def index(request):
    context = {
        'all_courses' : Courses.objects.all()
    }
    return render(request, 'index.html', context)

def add_course(request):
    if request.method != "POST":
        return redirect('/')

    errors = Courses.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
            messages.success(request, "Course unsuccessfully created")
        return redirect('/')
    else:
        new_course = Courses.objects.create(
            title = request.POST['title'],
            desc = request.POST['desc'],
            )
        new_course.save()
        return redirect ('/')

def destroy(request, course_id):
    queried_course = Courses.objects.get(id = course_id)
    context = {
        'queried_course' : queried_course
    }
    return render(request, 'delete.html', context)

def delete(request, course_id):
    queried_course = Courses.objects.get(id = course_id)
    queried_course.delete()
    return redirect ('/')

