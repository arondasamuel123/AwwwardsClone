from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Profile(models.Model):
    profile_photo = CloudinaryField('profile_photo')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    phone_number = models.IntegerField()
    
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()
        
    @classmethod
    def get_prof_id(cls,id):
        profile = cls.objects.filter(id=id).all()
        return profile
    def update_profile(self,bio):
        self.bio = bio
        self.save()
        
        
    
class Project(models.Model):
    project_title = models.CharField(max_length=20)
    project_description = models.CharField(max_length=20)
    project_screenshot = CloudinaryField('project_screenshot')
    project_link = models.URLField()
    date_posted = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    def save_project(self):
        self.save()
    @classmethod
    def search_by_project(cls, search_term):
        projects = cls.objects.filter(project_title__icontains=search_term)
        return projects
    @classmethod
    def get_proj_id(cls,id):
        project  = cls.objects.filter(id=id).all()
        return project
    
    def update_project(self, project_title):
        self.project_title = project_title
        self.save()
    
        

class Review(models.Model):
    design= models.IntegerField()
    usability = models.IntegerField()
    content = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def save_review(self):
        self.save()
    

    
    
