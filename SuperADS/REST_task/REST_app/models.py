from django.db import models

class logEntry(models.Model):
    ip = models.CharField(max_length=15)
    ua = models.CharField(max_length=256)
    geo = models.CharField(max_length=32)
    val = models.IntegerField()

class counter(models.Model):
    num = models.IntegerField()
