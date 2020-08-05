from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('a', views.processed, name='processed'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('gallery', views.gallery, name='gallery'),
    path('abc', views.abc, name='abc'),
    path('aboutus', views.aboutus, name='aboutus')
    ]
