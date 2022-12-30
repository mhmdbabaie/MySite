import email
from django.db import models

# Create your models here.
                                                                                

class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.name


class NewLetter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

        
