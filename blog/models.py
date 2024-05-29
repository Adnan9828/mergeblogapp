from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django_extensions.db.fields import AutoSlugField
from django.utils.timezone import now

class User(AbstractUser):
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to="my_images", blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}" if self.firstname and self.lastname else ""


class Catagory(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = AutoSlugField(max_length=100, unique=True, populate_from='name')
    
    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = AutoSlugField(max_length=100, unique=True, populate_from='name')
    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = AutoSlugField(max_length=100, unique=True, populate_from='title')
    thumbnail = models.ImageField(upload_to="my-thumbnail", blank=True, null=True)
    feature = models.ImageField(upload_to="my-feature", blank=True, null=True)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, blank=True, null=True)
    tag = models.ManyToManyField(Tags, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def  __str__(self):
        return self.title

class Comment(models.Model):
    sno = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null = True, blank = True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # name = models.CharField(max_length=250)
    body = models.TextField(max_length=500)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null = True, blank = True)
    # email = models.EmailField(unique=True)
    timestamp = models.DateTimeField(default=now)
    
    def __str__(self):
        return f'Comment by {self.user} on {self.post}'


class Reply(models.Model):
    sno = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null = True, blank = True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE, related_name="comment_replies")
    # name = models.CharField(max_length=250)
    body = models.TextField(max_length=500)
    # parent = models.ForeignKey('self', on_delete=models.CASCADE, null = True, blank = True)
    # email = models.EmailField(unique=True)
    timestamp = models.DateTimeField(default=now)
    
    def __str__(self):
        return f'Comment by {self.user} on {self.post} is {self.body}'
