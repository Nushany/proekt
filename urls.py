from django.urls import path
from . import views

urlpatterns = [
#    path('index/', views.index, name='home'),
    path('', views.index, name='home'),
    path('biology/', views.biology),
    path('chemistry/', views.chemistry),
    path('signup/', views.signup, name='signup'),
    path('list/', views.list, name='list'),
    path('profile/', views.profile, name='profile'),
    path('info/', views.info, name='info')
]