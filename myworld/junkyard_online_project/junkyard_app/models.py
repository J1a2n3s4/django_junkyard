from django.db import models

class product(models.Model):
  name = models.CharField(max_length=400)
  description = models.CharField(max_length=1000)
  image_url = models.CharField(max_length=300)
  link = models.CharField(max_length=200)
  price = models.FloatField(max_length=200)