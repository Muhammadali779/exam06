"""
URL Configuration for student_system project.
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('courses/', include('courses.urls')),
    path('students/', include('students.urls')),
    path('enrollments/', include('enrollments.urls')),
]
