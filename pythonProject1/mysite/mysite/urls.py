from django.contrib import admin
from django.urls import path, include

from shopapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shopapp.urls'))
]