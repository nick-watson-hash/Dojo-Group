from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField,EmailField, IntegerField, NullBooleanField
import re
import bcrypt

class User(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    email=EmailField()
    bank=models.IntegerField(default=1000) 
    hashpass=models.CharField(max_length=115)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class GOAT(models.Model):
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    full_name=models.CharField(max_length=25)
    api_id=models.IntegerField(default=00)
    creator=models.ForeignKey(User, related_name='uploader', on_delete=models.CASCADE, default = 00)
    favorite=models.ForeignKey(User, related_name='my_fav', on_delete=models.CASCADE, null=True)

class GOATdb(models.Model):
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    full_name=models.CharField(max_length=55)
    api_id=models.IntegerField(default=00)
    # user should not be able to favorite database players, we can create a button that will add an instace of the player to their roster and faovrite it

class Matchup(models.Model):
    goat1_id=models.IntegerField(default=00)
    goat2_id=models.IntegerField(default=00)
    user=models.ForeignKey(User, related_name='creator', on_delete=models.CASCADE)
    winner=models.IntegerField(default=00)


# Create your models here.
