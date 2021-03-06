from django.test import TestCase
from .models import Project,Profile,Review
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
    def test_get_proj_id(self):
        self.user_one.save()
        self.profile_one.save()
        self.project_one.save()
        self.project_one.get_proj_id(self.project_one.id)
        projects = Project.objects.all()
        self.assertTrue(len(projects)> 0)
        
    def test_update_project(self):
        self.user_one.save()
        self.profile_one.save()
        self.project_one.save()
        self.project_one.get_proj_id(self.project_one.id)
        self.project_one.update_project('GithubSearchAPI')
        self.assertTrue(self.project_one.project_title=='GithubSearchAPI')
    
    def test_delete_project(self):
        self.user_one.save()
        self.profile_one.save_profile()
        self.project_one.save_project()
        self.project_one.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)== 0)


class ProfileModelTestCase(TestCase):
    def setUp(self):
        self.user_john = User(username='john123',email='john@gmail.com', password='abcdef')
        self.profile_two = Profile(profile_photo='/path/image.png',user=self.user_john, bio='I am here to get validation.Jokes',phone_number='0712345678')
        
        
    def test_save_profile(self):
        self.user_john.save()
        self.profile_two.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    
    def test_delete_profile(self):
        self.user_john.save()
        self.profile_two.save_profile()
        self.profile_two.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)== 0)
        
    def test_update_bio(self):
        self.user_john.save()
        self.profile_two.save_profile()
        self.profile_two.get_prof_id(self.profile_two.id)
        self.profile_two.update_profile('This is an updated bio')
        self.assertTrue(self.profile_two.bio=='This is an updated bio')
        
    def test_get_prof_id(self):
        self.user_john.save()
        self.profile_two.save_profile()
        self.profile_two.get_prof_id(self.profile_two.id)
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
        

class ReviewModelTestCase(TestCase):
    def setUp(self):
        self.user_jane = User(username='jane123', email='jane123@gmail.com',password='qwerty@420')
        self.profile_jane = Profile(profile_photo='/image/png',user=self.user_jane,  bio='this is my bio',phone_number='0791019910')
        self.project_three = Project(project_title='Design Website', project_description='Website for fashion',project_screenshot='/path/image.png',profile=self.profile_jane)
        self.review_one = Review(design='1',usability='7',content='6',user=self.user_jane,project=self.project_three)
        
    def test_save_review(self):
        self.user_jane.save()
        self.profile_jane.save()
        self.project_three.save()
        self.review_one.save_review()
        reviews = Review.objects.all()
        self.assertTrue(len(reviews) > 0)
        
        
        