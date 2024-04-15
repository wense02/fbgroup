from django.db import models

# Create your models here.

class FacebookGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    member_count = models.IntegerField()
    is_private = models.BooleanField(default=True)
    town = models.TextField()
    location = models.CharField(max_length=200)
    # You may need additional fields like town, location, etc. based on your requirements


    def __str__(self):
        return self.name


class Town(models.Model):
    name = models.CharField(max_length=255)
    # You may include additional fields like location, population, etc. based on your requirements

    def __str__(self):
        return self.name

class FacebookGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    member_count = models.IntegerField()
    is_private = models.BooleanField(default=True)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    # You may need additional fields like location, category, etc. based on your requirements

    def __str__(self):
        return self.name


