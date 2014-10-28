from django.db import models

class testResults(models.Model):
    solution = models.TextField()
    prob = models.IntegerField()