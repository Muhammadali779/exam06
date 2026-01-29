from django.db import models
from django.core.exceptions import ValidationError


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    duration_weeks = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def clean(self):
        if self.duration_weeks <= 0:
            raise ValidationError({'duration_weeks': 'Duration must be greater than 0'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def get_enrolled_students_count(self):
        return self.enrollment_set.count()

    def delete(self, *args, **kwargs):
        if self.enrollment_set.exists():
            raise ValidationError("Bu kursga studentlar yozilgan. O'chirish mumkin emas.")
        super().delete(*args, **kwargs)
