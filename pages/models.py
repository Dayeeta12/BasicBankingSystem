from django.db import models

# Create your models here.
class Customers(models.Model):
    username = models.CharField(max_length=150, default='')
    email = models.CharField(max_length=150)
    gender = models.CharField(max_length=10)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    

    def __str__(self):
        return self.username

class Trans_hist(models.Model):
    sender = models.CharField(max_length=50)
    sender_id = models.CharField(max_length=50, default='')
    reciever = models.CharField(max_length=50) 
    reciever_id = models.CharField(max_length=50, default='')
    amount = models.FloatField()
    date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.sender + ' to ' + self.reciever
    


    