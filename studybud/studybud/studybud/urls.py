
from django.contrib import admin
from django.urls import path,include
#include is because of to know the django urls

from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    path('api/',include('base.api.urls'))
    
]
