from tkinter import N
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact-us', views.contact, name='contact'),
    path('about-us', views.about, name='about'),
    path('services', views.services, name='services'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('portfolio/<slug:slug>', views.portfoliodetail, name='portfoliodetail'),
    path('ongoing-project/<slug:slug>', views.GoingProject, name='GoingProject'),
    path('gallery', views.gallery, name='gallery')
]