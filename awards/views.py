from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm, ProfileForm, ProjectForm, RatingForm
from django.contrib.auth import login,logout,authenticate
from .models import Profile, Project, Review
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project
from .serializers import ProjectSerializer



def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {"projects":projects})

def signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            login(request,user)
            return redirect(create_profile)
    
    else:
        form = SignUpForm()
    return render(request,'auth/registration.html',{"form":form})

def signin(request):
    if request.method=='POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username,password=password)
            
            if user.is_active:
                login(request,user)
                return redirect(home)
            else:
                return "Your account is inactive"
    else:
        form = LoginForm()
    return render(request, 'auth/login.html',{"form":form})

def create_profile(request):
    current_user = request.user
    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save_profile()
            return redirect(home)
    else:
        form = ProfileForm()
    return render(request, 'auth/profile.html',{"form":form})
        
def user_profile(request, id):
    current_user = request.user
    profile = Profile.objects.filter(user_id=id).all()
    projects = Project.objects.filter(profile=current_user.profile.id).all()
    return render(request, 'view_profile.html',{"profile":profile, "projects":projects})

def post_project(request):
    current_user = request.user
    if request.method=="POST":
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = current_user.profile
            project.save_project()
            return redirect(home)
    else:
        form = ProjectForm()
    return render(request, 'post_project.html',{"form":form})

def search_project(request):
    if 'project'in request.GET and request.GET['project']:
        search_project = request.GET.get('project')
        searched_projects = Project.search_by_project(search_project)
        message = f'{search_project}'
        return render(request, 'search_project.html',{"projects":searched_projects, "message":message})
    
def rate_project(request, id):
    current_user = request.user
    project = Project.objects.get(pk=id)
    ratings = Review.objects.filter(project=project.id).all()
    if request.method=='POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = current_user
            rating.project = project
            rating.save_review()
            return redirect(home)
        
    else:
        form = RatingForm()
    return render(request, 'rating.html', {"form":form, "project":project, "ratings":ratings})

def project_details(request,id):
    project = Project.objects.get(pk=id)
    ratings = Review.objects.filter(project=project.id).all()
    design = Review.objects.filter(project=project.id).values_list('design',flat=True)
    usability = Review.objects.filter(project=project.id).values_list('usability',flat=True)
    content = Review.objects.filter(project=project.id).values_list('content',flat=True)
    total_design=0
    total_usability=0
    total_content = 0
    for score in design:
        total_design+=score
    for score in usability:
        total_usability+=score
    for score in content:
        total_content+=score
        
        
    total_score = (total_design + total_usability + total_content)/3
    return render(request, 'project_details.html',{"project":project, "ratings":ratings,"total_score":total_score})
        
class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)
      


def logout_view(request):
    logout(request)
    return redirect(home)