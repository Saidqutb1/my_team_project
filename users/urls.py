from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_painting, name='upload_painting'),
    path('profile/<int:pk>/', views.profile, name='profile'),
]
