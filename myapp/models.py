from collections import defaultdict
from django.db import models
from django.db.models.fields import NullBooleanField
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    company_name=models.CharField(max_length=25, null=True,)
    company_bio=models.CharField(max_length=200, null=True)
    company_about=models.TextField(max_length=500, null=True)
    company_email=models.CharField(max_length=200, null=True)
    company_phone=models.CharField(max_length=200, null=True)
    company_adress=models.CharField(max_length=200, null=True)
    company_website=models.CharField(max_length=200, null=True)
    company_instagram=models.CharField(max_length=200, null=True)
    company_facebook=models.CharField(max_length=200, null=True)
    company_pic=models.ImageField(upload_to='images/',null=True, blank=True )
    company_added=models.DateTimeField(auto_now_add=True, null=True)
    completed=models.BooleanField(default=False)
    owner=models.OneToOneField(User,null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.company_name
    

    class Meta:
        verbose_name='Companie'



        