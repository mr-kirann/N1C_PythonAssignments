from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ('', 'Choose gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
