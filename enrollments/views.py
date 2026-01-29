from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import IntegrityError
from .models import Enrollment
from .forms import EnrollmentForm


def enrollment_list(request):
    enrollments = Enrollment.objects.select_related('student', 'course').all()
    return render(request, 'enrollments/enrollment_list.html', {'enrollments': enrollments})


def enrollment_create(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Student kursga muvaffaqiyatli yozildi!')
                return redirect('enrollment_list')
            except IntegrityError:
                messages.error(request, 'Bu student allaqachon ushbu kursga yozilgan!')
    else:
        form = EnrollmentForm()
    return render(request, 'enrollments/enrollment_form.html', {'form': form})


def enrollment_delete(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == 'POST':
        enrollment.delete()
        messages.success(request, 'Ro\'yxatdan o\'chirish muvaffaqiyatli amalga oshirildi!')
        return redirect('enrollment_list')
    return redirect('enrollment_list')
