from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'digicraft.html')

def pricing(request):
  return render(request, 'pricing.html')

def contact(request):
  return render(request, 'contact.html')

def services(request):
  return render(request, 'services.html')

def about(request):
  return render(request, 'about.html')