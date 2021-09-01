from django.db import models
import re

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['title']) < 5:
            errors['title'] = "The course title should be at least 5 characters"
        if len(postData['desc']) < 15:
            errors['desc'] = "The course description should be at least 15 characters"
        return errors

class Courses(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(default=None)
    date_added = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

    def __repr__(self):
        return f"<User object: {self.title} ({self.id})>"