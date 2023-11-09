from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
# Create your models here.

# Project model 
class Project(models.Model):
    owner = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default= 'default.jpg')
    demo_link = models.CharField(max_length=1000, null=True, blank=True)
    source_code = models.CharField(max_length=1000, null=True, blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True)  # Stringfy the model if it is defined below
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            img = self.featured_image.url
        except:
            img = ''
        return img

# A review model for the project 
class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'up'),
        ('down', 'down'),
    )
    # owner
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=50, choices=VOTE_TYPE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value


# Tag model for the project like django, react, python, java etc
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    username = models.CharField(unique=True, max_length=200)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    skills = models.ManyToManyField(Tag, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, default='default.jpg')

    REQUIRED_FIELDS = []