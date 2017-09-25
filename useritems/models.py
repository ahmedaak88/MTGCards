from django.db import models
from mainapp.models import Cards
from django.contrib.auth.models import User


class CartItem(models.Model):
	cart = models.ForeignKey("Cart")
	items = models.ForeignKey(Cards)
	quantity = models.PositiveIntegerField(default=1)
	def __str__(self):
		return self.items.name



class Cart(models.Model):
	user = models.ForeignKey(User)
	items = models.ManyToManyField(Cards , through=CartItem)
	def __str__(self):
		return self.user.username
