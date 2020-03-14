from django.test import TestCase
from .models import Project,Profile
from django.contrib.auth.models import User


class ProjectModelTestCase(TestCase):
    '''
    Test Class for Project Model
    '''
    def setUp(self):
        self.user_one = User(username='arondasamuel123', email='arondasamuel123@gmail.com', password='123456')
        self.profile_one = Profile(profile_photo='path/image.png',user=self.user_one, bio="I am great developer",phone_number='0791019910')
        self.project_one = Project(project_title='GithubSearch', project_description='Project one', project_link='/path/screenshot.png',profile=self.profile_one)
        
        
    def test_save_project(self):
        self.user_one.save()
        self.profile_one.save()
        self.project_one.save_project()
        
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)
    
    def test_search_project(self):
        self.user_one.save()
        self.profile_one.save()
        self.project_one.save_project()
        
        projects = self.project_one.search_by_project('GithubSearch')
        self.assertTrue(len(projects) > 0)  

