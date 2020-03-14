from django.db import models
from cloudinary import CloudinaryField
from django.contrib.auth.models import User

class Profile(models.Model):
    profile_photo = CloudinaryField('profile_photo')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    phone_number = models.IntegerField()
    email = models.EmailField()
    
class Project(models.Model):
    project_title = models.CharField(max_length=20)
    project_description = models.CharField(max_length=20)
    project_screenshot = CloudinaryField('project_screenshot')
    project_link = models.URLField()
    date_posted = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    

    
    
