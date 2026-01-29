from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Course
from .forms import CourseForm


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Kurs muvaffaqiyatli yaratildi!')
                return redirect('course_list')
            except ValidationError as e:
                for field, errors in e.message_dict.items():
                    for error in errors:
                        messages.error(request, f'{field}: {error}')
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {'form': form, 'action': 'Yaratish'})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    enrollments = course.enrollment_set.select_related('student').all()
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'enrollments': enrollments
    })


def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Kurs muvaffaqiyatli yangilandi!')
                return redirect('course_detail', pk=pk)
            except ValidationError as e:
                for field, errors in e.message_dict.items():
                    for error in errors:
                        messages.error(request, f'{field}: {error}')
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/course_form.html', {
        'form': form,
        'action': 'Tahrirlash',
        'course': course
    })


def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        try:
            course.delete()
            messages.success(request, 'Kurs muvaffaqiyatli o\'chirildi!')
            return redirect('course_list')
        except ValidationError as e:
            messages.error(request, str(e))
            return redirect('course_detail', pk=pk)
    return redirect('course_list')
