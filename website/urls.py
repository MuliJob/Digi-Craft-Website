from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='digicraft'),
    path('pricing/', views.pricing, name = 'pricing'),
    path('contactus/', views.contact, name = 'contact'),
    path('services/', views.services, name= 'services'),
    path('about/', views.about, name = 'about'),
    path(r'ajax/newsletter/', views.newsletter, name='newsletter')
]