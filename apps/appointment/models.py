from django.db import models


class Doctor(models.Model):
    DEPARTMENT_CHOICES = [
        ('primary_care', 'Primary Care'),
        ('pediatrics', 'Pediatrics'),
        ('internal_medicine', 'Internal Medicine'),
        ('cardiology', 'Cardiology'),
        ('neurology', 'Neurology'),
        ('ob_gyn', 'Obstetrics and Gynecology'),
        ('orthopedics', 'Orthopedics'),
        ('dermatology', 'Dermatology'),
    ]
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255, choices=DEPARTMENT_CHOICES)
    specialization = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    bio = models.TextField()
    photo = models.ImageField(upload_to='doctors/', default='static/img/avatar.png')
    url = models.URLField()

    def __str__(self):
        return self.name
