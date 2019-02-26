from __future__ import unicode_literals
from django.db import models
from apps.login_app.models import User
import re
nameregex=re.compile(r'^[a-zA-Z]+$')


class Job_Manager(models.Manager):
    def edit_validator(self, postData):
        errors = {}
        
        if len(postData['title']) == 0:
            errors['title'] = "Title cannot be blank."
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 letters."
        if not nameregex.match(postData['title']):
            errors['title'] = "Title must contain letters only."
        if len(postData['description']) == 0:
            errors['description'] = "Description cannot be blank"
        if len(postData['description']) < 2:
            errors["description"] = "Description should be at least 2 letters."
        if not nameregex.match(postData['description']):
            errors['description'] = "Description must contain letters only."
        if len(postData['location']) == 0:
            errors['location'] = "Location cannot be blank"
        if len(postData['location']) < 2:
            errors["location"] = "Location should be at least 2 letters."
        return errors
    def add_validator(self, postData):
        errors = {}
        
        if len(postData['title']) == 0:
            errors['title'] = "Title cannot be blank."
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 letters."
        if len(postData['description']) == 0:
            errors['description'] = "Description cannot be blank"
        if len(postData['description']) < 2:
            errors["description"] = "Description should be at least 2 letters."
        if len(postData['location']) == 0:
            errors['location'] = "Location cannot be blank"
        if len(postData['location']) < 2:
            errors["location"] = "Location should be at least 2 letters."
        return errors
class Job(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    user = models.ForeignKey(User, related_name="jobs")
    my_job = models.ManyToManyField(User, related_name="my_job")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Job_Manager()

