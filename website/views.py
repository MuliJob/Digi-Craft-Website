from django.shortcuts import render
from .models import NewsLetterRecipients
from django.http import Http404, JsonResponse
from .email import send_welcome_email

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
    email = request.POST.get('email')
    if NewsLetterRecipients.objects.filter(email=email).exists():
        data = {'error': 'This email is already subscribed to the mailing list'}
    else:
        recipient = NewsLetterRecipients(email=email)
        recipient.save()
        send_welcome_email(email)
        data = {'success': 'You have been successfully added to the mailing list'}
    return JsonResponse(data)