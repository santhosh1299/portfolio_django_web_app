from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to='Portfolio/images/')
    url=models.URLField(blank=True)
    def __str__(self):
        return self.title
    
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="Message", widget=forms.Textarea)