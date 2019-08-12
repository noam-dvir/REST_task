from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

urlpatterns = [
    url(r'^',include('REST_app.urls')),
    url(r'^getID/',include('REST_app.urls')),
    url(r'^showDB/',include('REST_app.urls')),
    path('admin/', admin.site.urls),
]
