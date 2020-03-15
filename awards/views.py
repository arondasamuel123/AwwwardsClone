from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm, ProfileForm
from django.contrib.auth import login,logout,authenticate
from .models import Profile



def home(request):
    
    return render(request, 'home.html')

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


def logout_view(request):
    logout(request)
    return redirect(home)