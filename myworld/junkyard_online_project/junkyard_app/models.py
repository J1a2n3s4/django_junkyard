from django.db import models

class product(models.Model):
  name = models.CharField(max_length=400)
  description = models.CharField(max_length=1000)
  image_url = models.CharField(max_length=300)
  link = models.CharField(max_length=200)

class kontakt(models.Model):
  tel = models.CharField(max_length=21)
  email = models.CharField(max_length=400)