from django.db import models
from datetime import *
import bcrypt
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        existing_users = Users.objects.filter(email=postData['email'])
        formatteddate = datetime.strptime(postData['date_of_birth'], '%Y-%m-%d')

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
        if formatteddate >= datetime.now():
            errors['date_of_birth'] = "Your birthday should be in the past"
        if len(postData['password']) < 8:
            errors['password'] = "Your password should be at least 8 characters"
        if (postData['password'] != postData['confirm']):
            errors['confirm'] = "Your passwords do not match"
        return errors

    def login_validator(self, postData):
        errors = {}
        existing_users = Users.objects.filter(email=postData['login_email'])
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

    def postcomment_validator(self, postData):
        errors = {}
        if len(postData['message']) == 0:
            errors['message'] = "You must enter some characters in order to leave a comment"
        if len(postData['comment']) == 0:
            errors['comment'] = "You must enter some characters in order to leave a comment"
        return errors


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    date_of_birth = models.DateTimeField(null=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Message(models.Model):
    message = models.TextField(max_length=255)
    user = models.ForeignKey(Users, related_name="user_message", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField(max_length=255)
    message = models.ForeignKey(Message, related_name="message_comments", on_delete=models.CASCADE)
    user = models.ForeignKey(Users, related_name="user_comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
