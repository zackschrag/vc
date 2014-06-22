from django.db import models
from django.contrib.auth.models import User

class Chapter(models.Model):
	chapter_name = models.CharField(max_length=100)
