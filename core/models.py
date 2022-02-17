from django.db import models
from django.db.models import Model
# Create your models here.

class User(Model):
	fname = models.CharField(max_length = 100)
	lname = models.CharField(max_length = 100)
	email = models.EmailField(max_length = 200)
	textfield = models.CharField(max_length = 500)
