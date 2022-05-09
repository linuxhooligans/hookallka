from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from hookallka import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
]
