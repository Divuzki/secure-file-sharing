from django.contrib.auth.models import AbstractUser
from django.db import models
from django_cryptography.fields import encrypt

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    date_of_birth = encrypt(models.DateField(null=True, blank=True))
    address = encrypt(models.TextField(null=True, blank=True))
    phone = encrypt(models.CharField(max_length=20, null=True, blank=True))
    
    class Meta:
        permissions = [
            ("view_student_records", "Can view student records"),
            ("edit_grades", "Can edit grades"),
            ("manage_courses", "Can manage courses"),
        ]

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"