from django.shortcuts import render
from .models import NewsLetterRecipients, Message
from django.http import JsonResponse
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
        data = {'success': 'Welcome aboard! 🚀 Thank you for subscribing to our newsletter! 🎉'}
    return JsonResponse(data)

def message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        try:
            additional_message = Message(
                name=name,
                email=email,
                phone=phone,
                message=message
            )

            additional_message.save()

            return JsonResponse({'success': 'We have received your message 🤝. We will contact you soon. 🤖'})
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)
