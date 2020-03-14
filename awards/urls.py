from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.signup,name='sign-up'),
    path('accounts/login/', views.signin,name='login'),
    path('logout/', views.logout_view,name='logout')
]