from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('example/', views.example, name='example'),
    path('record/', views.record, name='record'),
    path('search_window/', views.search_window, name='search_window'),
    path("door/", views.door, name="door"),
    path("ending/", views.ending, name='ending'),
    path('lab', views.lab, name='lab'),
    path('desk', views.desk, name='desk'),
    path('monitor', views.monitor, name='monitor'),
    path('drawer', views.drawer, name='drawer'),

]
