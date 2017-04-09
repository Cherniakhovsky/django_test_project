from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^about/',views.about, name='about'),
    #url(r'^register/',views.register,name='register'),
]