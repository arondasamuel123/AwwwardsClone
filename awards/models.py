from django.db import models
from cloudinary import CloudinaryField
from django.contrib.auth.models import User

class Profile(models.Model):
    profile_photo = CloudinaryField('profile_photo')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    phone_number = models.IntegerField()
    email = models.EmailField()
    

    
    
