from django.db import models

# Create your models here.

class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class Register(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    C_password = models.CharField(max_length=100)

    def __str__(self):
        return self.email