from django.db import models
from django.contrib.auth.models import User



class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Profile(models.Model):
    """
    User Profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    bio = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length=30, blank=True)
    dob = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(default='images_1.png', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username
