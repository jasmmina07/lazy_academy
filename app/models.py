from django.db import models

# Create your models here.

class Question(models.Model):
    a=models.CharField(max_length=30)
    b=models.CharField(max_length=30)
    c=models.CharField(max_length=30)

    def __str__(self):
        return self.c

class Users(models.Model):
    first_name=models.TextField()
    last_name=models.TextField()
    user_name=models.CharField(max_length=30)
    password=models.TextField()
    email=models.EmailField()

    def __str__(self):
        return self.first_name+" "+self.last_name

   