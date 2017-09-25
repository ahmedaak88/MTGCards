from django.conf.urls import url
from . import views



urlpatterns = [

    url(r'^allcarts/$', views.allcarts, name="allcarts"),




]
