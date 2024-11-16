from django.urls import path
from.import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('mans/', views.mans, name='mans'),
    path('contact/', views.contact, name='contact'),
    path('woman/', views.woman, name='woman'),
    path('computer/', views.computer, name='computer'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),


]