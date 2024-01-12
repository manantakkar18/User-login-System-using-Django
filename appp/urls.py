from django.urls import path
from  appp import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logout, name = 'logout')
]