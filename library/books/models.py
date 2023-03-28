from django.db import models

# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=20)
    author=models.CharField(max_length=20,default='Guest')
    picture=models.ImageField()
    email=models.EmailField(blank=True)
    desc=models.TextField(default='Available in lict Library')
    def __str__(self):
        return self.name
