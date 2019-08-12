from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^getID/$',views.DBID,name='DBID'),
    url(r'^showDB/$',views.showDB,name='showDB'),

]
