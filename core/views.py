from django.shortcuts import render
from courses.models import Course
from students.models import Student
from enrollments.models import Enrollment


def home(request):
    context = {
        'total_courses': Course.objects.count(),
        'total_students': Student.objects.count(),
        'total_enrollments': Enrollment.objects.count(),
    }
    return render(request, 'home.html', context)
