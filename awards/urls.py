from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.signup,name='sign-up'),
    path('accounts/login/', views.signin,name='login'),
    path('create/profile',views.create_profile, name='create-profile'),
    path('profile/<int:id>',views.user_profile, name='view-profile'),
    path('logout/', views.logout_view,name='logout')
]