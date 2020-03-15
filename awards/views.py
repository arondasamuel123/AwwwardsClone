from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm, ProfileForm, ProjectForm, RatingForm
from django.contrib.auth import login,logout,authenticate
from .models import Profile, Project



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
    profile = Profile.objects.filter(user_id=id).all()
    return render(request, 'view_profile.html',{"profile":profile})

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
    return render(request, 'rating.html', {"form":form, "project":project})
        
    


def logout_view(request):
    logout(request)
    return redirect(home)