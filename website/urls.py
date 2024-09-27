from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='digicraft'),
    path('pricing/', views.pricing, name = 'pricing'),
    path('contactus/', views.contact, name = 'contact'),
    path('services/', views.services, name= 'services'),
    path('about/', views.about, name = 'about'),
    path('services/details', views.details, name = 'details'),
    path(r'newsletter/subscribe/', views.newsletter, name='newsletter'),
    path(r'contact/sendmessage/', views.message, name='message')
]