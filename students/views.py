from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.models import Q
from .models import Student
from .forms import StudentForm


def student_list(request):
    students = Student.objects.all()
    
    # Search filter
    search = request.GET.get('search', '')
    if search:
        students = students.filter(
            Q(full_name__icontains=search) | Q(email__icontains=search)
        )
    
    # Age filter
    min_age = request.GET.get('min_age', '')
    if min_age:
        try:
            students = students.filter(age__gte=int(min_age))
        except ValueError:
            pass
    
    return render(request, 'students/student_list.html', {
        'students': students,
        'search': search,
        'min_age': min_age
    })


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Student muvaffaqiyatli yaratildi!')
                return redirect('student_list')
            except ValidationError as e:
                for field, errors in e.message_dict.items():
                    for error in errors:
                        messages.error(request, f'{field}: {error}')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form, 'action': 'Yaratish'})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    enrollments = student.enrollment_set.select_related('course').all()
    return render(request, 'students/student_detail.html', {
        'student': student,
        'enrollments': enrollments
    })


def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Student muvaffaqiyatli yangilandi!')
                return redirect('student_detail', pk=pk)
            except ValidationError as e:
                for field, errors in e.message_dict.items():
                    for error in errors:
                        messages.error(request, f'{field}: {error}')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {
        'form': form,
        'action': 'Tahrirlash',
        'student': student
    })


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student muvaffaqiyatli o\'chirildi!')
        return redirect('student_list')
    return redirect('student_list')
