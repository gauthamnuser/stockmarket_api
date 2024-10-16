from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("topgainers", views.topgainers, name="topgainers"),
    path("toplosers", views.toplosers, name="toplosers"),
    path("companydetails/<company_symbol>", views.companydetails, name='companydetails'),
    path("companydetails/", views.backhome, name='backhome')
]