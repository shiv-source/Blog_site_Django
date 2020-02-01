from django.urls import path
from .views import home,hello,login_view,register,blog_post
from django.conf.urls import url


urlpatterns = [
    path('',home, name="home"),
    url(r'^register',register,name="register"),
    url(r'^hello$',hello, name="hello"),
    url(r'^login',login_view,name="login"),
    url(r'^blog',blog_post,name="blog_post"),
   
]
