from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/$', views.usersignup, name="signup"),
    url(r'^login/$', views.userlogin, name="login"),
    url(r'^logout/$', views.userlogout, name="logout"),
    url(r'^home/$', views.post_home, name="home"),
    url(r'^listofcards/$', views.list_of_cards, name="listofcards"),
]
