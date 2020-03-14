from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth import login



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