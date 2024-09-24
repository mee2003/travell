from . import views
from django.urls import path

urlpatterns = [

    path('',views.index,name='index'),
    # path('add/', views.addition, name='addition'),
    path('contact/', views.contact, name='contact'),
    # path('index1/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('elements/', views.elements, name='elements'),
    path('destinations/', views.destinations, name='destinations'),

    path('news/', views.news, name='news'),
    # path('thanks/', views.thanks, name='thanks'),

]