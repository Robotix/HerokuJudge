from django.db import models

class sol(models.Model):
    id = models.AutoField(primary_key=True)
    solution = models.TextField()
    lang = models.CharField(max_length=5)
    email = models.EmailField(max_length=254)
    queries =models.IntegerField()