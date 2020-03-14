from django.shortcuts import render,redirect
from .forms import SignUpForm,LoginForm
from django.contrib.auth import login,logout,authenticate



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
            return redirect(home)
    
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


def logout_view(request):
    logout(request)
    return redirect(home)