from django.db import models
from users.models import User

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    teacher = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'role': 'teacher'}
    )
    students = models.ManyToManyField(
        User,
        related_name='enrolled_courses',
        limit_choices_to={'role': 'student'}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CourseAccessLog(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accessed_at = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=50)

    class Meta:
        ordering = ['-accessed_at']