from django.db import models

# Create your models here.

class Testcase(models.Model):
	id = models.IntegerField(
		primary_key = True)
	bunker_number = models.IntegerField()
	bunker_length = models.CommaSeparatedIntegerField(
		max_length=100000)
	image = models.ImageField()

	def __unicode__(self):
		return str(id)
