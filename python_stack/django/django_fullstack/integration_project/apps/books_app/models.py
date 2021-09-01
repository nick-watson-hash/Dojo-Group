from django.db import models
from datetime import *
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

    def book_validator(self, postData):
        errors = {}
        if len(postData['bookTitle']) == 0:
            errors['bookTitle'] = "You must enter some characters in the title field"
        if len(postData['bookDescription']) < 5:
            errors['bookDescription'] = "The book description must be at least 5 characters"
        if len(postData['bookDescription']) == 0:
            errors['bookDescription'] = "You must enter some characters in the description field"
        return errors

    def edit_validator(self, postData):
        errors = {}
        if len(postData['bookDescriptionEdit']) < 5:
            errors['bookDescriptionEdit'] = "The book description must be at least 5 characters"
        if len(postData['bookDescriptionEdit']) == 0:
            errors['bookDescriptionEdit'] = "You must enter some characters in the description field"
        return errors
        errors = {}


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    #fav_book
    #liked_books

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    creator = models.ForeignKey(User, related_name="fav_book", on_delete=models.CASCADE, null=True)
    users_fav = models.ManyToManyField(User, related_name="liked_book")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()