from django.db import models

class Dummy(models.Model):
	name = models.CharField(max_length=200)
	age = models.IntegerField()