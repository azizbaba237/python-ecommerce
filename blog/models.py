from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create class Category
class Category(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name

# Create class Article 
class Article(models.Model):
    user      = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title     = models.CharField(max_length=50)
    Category  = models.ForeignKey(Category, on_delete=models.CASCADE)
    des       = models.TextField()
    image     = models.ImageField(null=True, blank=True)   
    create_at = models.DateTimeField(auto_now_add=True)
    upload_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("my-articles")
