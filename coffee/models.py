from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Coffee(models.Model):
    title=models.CharField(max_length=255,null=False,blank=True)
    purchaser=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    price=models.CharField(max_length=255,null=False,blank=False)
    reviewer=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    name=models.CharField(max_length=255,null=False,blank=False)
    reviewer=models.TextField()
    
    def __str__(self):
        return self.name