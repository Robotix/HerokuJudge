from django.db import models

class sol(models.Model):
    solution = models.TextField()
    lang = models.CharField(max_length=5)
    prob = models.IntegerField()
    team_id = models.IntegerField()
    stdout =models.TextField(blank=True, null=True)
