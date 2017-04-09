from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Client(models.Model):
    username = models.OneToOneField(User)
    #first_name = models.CharField(max_length=20)
    #last_name = models.CharField(max_length=20)
    #email = models.EmailField(max_length=25)
    passport_number = models.CharField(max_length=20,unique=True)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.passport_number



class Cost(models.Model):
    username = models.ForeignKey(User)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    cost_description = models.CharField(max_length=128)
    cost = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.balance