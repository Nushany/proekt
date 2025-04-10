from django.urls import path
from . import views

urlpatterns = [
#    path('index/', views.index, name='home'),
    path('', views.index, name='home'),
    path('/shopapp/biology/', views.biology),
    path('/shopapp/chemistry/', views.chemistry),
    path('/shopapp/signup/', views.signup, name='signup'),
    path('/shopapp/list/', views.list, name='list'),
    path('/shopapp/profile/', views.profile, name='profile'),
    path('/shopapp/info/', views.info, name='info')
]
