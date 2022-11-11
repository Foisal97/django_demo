from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name 

# Create your models here.
class Room(models.Model):
    name= models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    


    def ___str__(self):
        return self
        


class Message(models.Model):
    
    room =  models.ForeignKey(Topic, on_delete=models.CASCADE)
    body = models.TextField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]

    
    