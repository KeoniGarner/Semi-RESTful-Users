from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validations(self, postData):
        errors = {}
        if len(postData["first_name"]) < 2:
            errors["first_name"] = "First name should be more than 2 characters"
        if len(postData["last_name"]) < 2:
            errors["last_name"] = "Last name should be more than 2 characters"
        if len(postData["email"]) < 7:
            errors["email"] = "Email should be more than 7 characters"
        if "@" not in postData["email"] or "." not in postData["email"]:
            errors["email"] = "Email should be a valid email address"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    objects = UserManager()