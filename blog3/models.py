from django.db import models
from django.contrib.auth.models import User
from django.db import IntegrityError


# class Login(models.Model):
# 	name = models.CharField(max_length=200)
# 	password = models.CharField(max_length=200)
# 	email = models.EmailField(max_length=200)
# 	first_name = models.CharField(max_length=200)
# 	last_name = models.CharField(max_length=200)
# 	city = models.CharField(max_length=200)


class Post(models.Model):
	user = models.CharField(max_length=200,default='admin')
	tittle = models.CharField(max_length=200)
	slug = models.SlugField(unique=True,max_length=200)
	description = models.CharField(max_length=200)
	content = models.TextField(max_length=200)
	published = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)


# Create your models here.
