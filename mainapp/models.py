from django.db import models



class Cards(models.Model):
	name = models.CharField(max_length=300)
	text = models.TextField(null=True)
	image= models.URLField(max_length=300,null=True)

	def __str__(self):
		return self.name
