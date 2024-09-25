from django.db import models

# Create your models here.
class NewsLetterRecipients(models.Model):
    email = models.EmailField()