from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData[title]) < 5:
            errors['title'] = "Movie title name should be at least 5 characters"
        if len(postData[desc]) < 5:
            errors['desc'] = "Movie title name should be at least 5 characters"
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField(auto_now=True)
    desc = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
    
    def __repr__(self):
        return f"<User object: {self.title} ({self.id})>"