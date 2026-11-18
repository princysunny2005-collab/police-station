from django.urls import path
from crime import views

urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("service/",views.service ,name="service"),
    path("public/",views.public,name="public"),
    path("news/",views.news,name="news"),
    path("gallary/",views.gallary,name="gallary"),
    path("contact/",views.contact,name="contact"),
    path("complaint",views.complaint,name="complaint"),
    path("dashboard/",views.dashboard,name="dashboard")
]
