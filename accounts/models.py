from django.db import models
from base import BaseModel
from django.contrib.auth.models import User
from core.models import *


# Create your models here.

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    is_email_verified = models.BooleanField(default=True)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile', blank= True)


    def __str__(self):
        return self.user.username

    def total_post(self):
        return BlogPost.objects.all().count()

    def total_category(self):
        return Category.objects.all().count()


