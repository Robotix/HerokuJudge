from django.db import models

class sol(models.Model):
    solution = models.TextField()
    lang = models.CharField(max_length=5)
    prob = models.IntegerField()
    email = models.EmailField(max_length=254)
    queries =models.IntegerField()