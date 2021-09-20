from django.db import models
import bcrypt
import re
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        existing_users = User.objects.filter(email=postData['email'])

        if len(postData['first_name']) < 2:
            errors['first_name'] = "Your first name should be at least 2 characters with only letters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Your last name should be at least 2 characters with only letters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
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
        elif bcrypt.checkpw(postData['login_pass'].encode(), existing_users[0].password.encode()) != True:
            errors ['login_pass'] = "Incorrect email or password"
        return errors

class QuoteManager(models.Manager):
    def quote_validator(self, postData):
        errors = {}
        if len(postData['quoteAuthor']) == 0:
            errors['quoteAuthor'] = "You must enter some characters in the author field"
        if len(postData['quoteAuthor']) < 2:
            errors['quoteAuthor'] = "You must enter some characters in the author field"
        if len(postData['quoteMessage']) < 10:
            errors['quoteMessage'] = "The quote description must be at least 10 characters"
        if len(postData['quoteMessage']) == 0:
            errors['quoteMessage'] = "You must enter some characters in the description field"
        return errors

    def edit_validator(self, postData):
        errors = {}
        if len(postData['quoteAuthorEdit']) == 0:
            errors['quoteAuthorEdit'] = "You must enter some characters in the author field"
        if len(postData['quoteAuthorEdit']) < 2:
            errors['quoteAuthorEdit'] = "You must enter some characters in the author field"
        if len(postData['quoteMessageEdit']) < 10:
            errors['quoteMessageEdit'] = "The quote description must be at least 10 characters"
        if len(postData['quoteMessageEdit']) == 0:
            errors['quoteMessageEdit'] = "You must enter some characters in the description field"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    #quote_creator
    #fav_quotes

class Quote(models.Model):
    author = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    creator = models.ForeignKey(User, related_name="quote_creator", on_delete=models.CASCADE, null=True)
    users_fav = models.ManyToManyField(User, related_name="fav_quotes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()