
from django.contrib import admin
from django.urls import path,include
#include is because of to know the django urls
from django.views.static import serve
from django.conf.urls import url

from django.urls import path,include
from django.conf import Settings
from django.urls.static import static
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    path('api/',include('base.api.urls'))

    url(r'^media/(?P<path>.*)$', serve,{'document_root':  settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    
]
