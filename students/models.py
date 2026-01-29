from django.db import models
from django.core.exceptions import ValidationError


class Student(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.full_name

    def clean(self):
        if self.age < 16:
            raise ValidationError({'age': 'Age must be at least 16'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def get_enrolled_courses_count(self):
        return self.enrollment_set.count()
