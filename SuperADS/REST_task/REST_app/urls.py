from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls import url,include

router = routers.DefaultRouter()
router.register('log', views.EntryView)
#router.register('getId', views.getID)

urlpatterns = [
    #path('', include('REST_app.urls'))
    #url(r'^getId/$',views.getID,name='getID'),
    url(r'^$',views.index,name='index'),
    url(r'^getID/$',views.DBID,name='DBID'),

    #path('', include(router.urls))

]
