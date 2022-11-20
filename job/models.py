from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class StudentUser(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    mobile = PhoneNumberField(max_length=15, null=False)
    image = models.ImageField(null=True)
    gender = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.user.username



class Recruiter(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    mobile = PhoneNumberField(max_length=15, null=False)
    image = models.ImageField(null=True)
    gender = models.CharField(max_length=10, null=True)
    company = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=10, null=True, blank=True)


    def __str__(self):
        return self.user.username