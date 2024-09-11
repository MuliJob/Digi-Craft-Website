from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
        'title': 'Welcome to My Django Site',
        'message': 'This is the home page at the root URL.',
    }
  return render(request, 'digicraft.html', context)