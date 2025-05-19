from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from courses.models import Course
from users.models import User

class Grade(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'}
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='grades_created'
    )

    class Meta:
        unique_together = ['student', 'course']
        permissions = [
            ("view_own_grades", "Can view own grades"),
        ]

    def __str__(self):
        return f"{self.student.username} - {self.course.name}: {self.score}"

class GradeChangeLog(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    previous_score = models.DecimalField(max_digits=5, decimal_places=2)
    new_score = models.DecimalField(max_digits=5, decimal_places=2)
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    changed_at = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()

    class Meta:
        ordering = ['-changed_at']