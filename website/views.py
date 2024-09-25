from django.shortcuts import render
from .models import NewsLetterRecipients
from django.http import Http404, JsonResponse

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

def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)