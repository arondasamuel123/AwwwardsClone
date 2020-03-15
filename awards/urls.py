from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.signup,name='sign-up'),
    path('accounts/login/', views.signin,name='login'),
    path('create/profile',views.create_profile, name='create-profile'),
    path('profile/<int:id>',views.user_profile, name='view-profile'),
    path('submit/project/',views.post_project, name='post-project'),
    path('search/', views.search_project,name='search-project'),
    path('rating/<int:id>',views.rate_project, name='rate-project'),
    path('project/<int:id>',views.project_details,name='project-details'),
    path('logout/', views.logout_view,name='logout')
]