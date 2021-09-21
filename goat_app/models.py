from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField,EmailField, IntegerField, NullBooleanField
import re
import bcrypt

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        existing_users = User.objects.filter(email=postData['email'])
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postData['first_name']) < 2:
            errors['first_name'] = "Your first name should be at least 2 characters with only letters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Your last name should be at least 2 characters with only letters"
        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ('The email address is not in the correct format')
        if len(existing_users) != 0:
            errors['email'] = "Your email that you have chosen cannot be used"
        if len(postData['password']) < 8:
            errors['password'] = "Your password should be at least 8 characters"
        if (postData['password'] != postData['confirm']):
            errors['confirm'] = "Your passwords do not match"
        return errors

    def login_validator(self, postData):
        errors = {}
        existing_users = User.objects.filter(email=postData['login_email'])
        if len(postData['login_email']) == 0:
            errors ['login_email'] = "Your login email needs to be entered"
        if len(postData['login_pass']) == 0:
            errors ['login_pass'] = "Your password needs to be entered"
        if len(postData['login_pass']) < 8:
            errors ['login_pass'] = "An eight character password must be entered"
        if not existing_users:
            errors ['login_pass'] = "Incorrect email or password"
        elif bcrypt.checkpw(postData['login_pass'].encode(), existing_users[0].hashpass.encode()) != True:
            errors ['login_pass'] = "Incorrect email or password"
        return errors

    def bet_validator_custom(self, postData):
        return self._extracted_from_bet_validator_random_2(postData, 'bet_custom')

    def bet_validator_random(self, postData):
        return self._extracted_from_bet_validator_random_2(postData, 'bet_random')

    def _extracted_from_bet_validator_random_2(self, postData, arg1):
        errors = {}
        if postData[arg1] == '':
            errors[arg1] = 'Enter a bet, coward'
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    email=EmailField()
    bank=models.IntegerField(default=1000) 
    hashpass=models.CharField(max_length=115)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = UserManager()

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
