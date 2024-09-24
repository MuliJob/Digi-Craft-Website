from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='digicraft'),
    path('pricing/', views.pricing,name = 'pricing'),
]