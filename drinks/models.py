from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.urls import reverse

class blogPost(models.Model):
    title = models.CharField(max_length=200,)
    des = models.TextField()
    date_create = models.DateField(auto_now_add=True)
    date_modefied = models.DateField(auto_now=True)
    user = models.ForeignKey(to=get_user_model(),on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    
    
    def c(self):
        return reverse('detail', kwargs={'pk': self.pk})
    
    
    
    
    def __str__(self):
        return f"{self.title}  {self.des}"
    
    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'pk': self.pk})
    
    
    
    
class comments(models.Model):
    OSTAN_IRAN = [
        ("tehran","تهران"),
        ("gillan","گیلان"),
        ("alborz","البرز"),
    ]
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True,blank=True)
    adrees = models.TextField(max_length=300 ,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    ostan = models.CharField(max_length=255,choices=OSTAN_IRAN)
    zipcode = models.CharField(max_length=100,null=True,blank=True)
    hideusers = models.BooleanField(default=True)
    comment = models.TextField()
    postoa = models.ForeignKey(to=blogPost,on_delete=models.CASCADE)
    
    
    def  __str__(self):
        return self.name