from django.db import models

# Create your models here.
class NewsLetterRecipients(models.Model):
    email = models.EmailField()

class Message(models.Model):
    name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=10,blank=False)
    message = models.CharField(max_length=1000, blank=False)

    def __str__(self):
        return self.name