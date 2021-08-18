from django.db import models
from datetime import datetime, time
import re

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        # EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # if not EMAIL_REGEX.match(postData['email']):
        #     errors['email'] = ("Invalid email address!")
        print(type(datetime.now()))
        print(type(postData['release_date']))
        if len(postData['title']) < 2:
            errors['title'] = "Movie title should be at least 2 characters"
        if len(postData['network']) < 2:
            errors['network'] = "Network title name should be at least 2 characters"
        if len(postData['release_date']) == 0:
            errors['release_date'] = "The release date needs to be entered or needs to be in the past"
        if len(postData['desc']) < 10:
            errors['desc'] = "Movie title description should be at least 10 characters"
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField(null=True)
    desc = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
    
    def __repr__(self):
        return f"<User object: {self.title} ({self.id})>"