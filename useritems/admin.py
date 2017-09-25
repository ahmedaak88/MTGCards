from __future__ import unicode_literals
from django.contrib import admin
from .models import Cart

class CartModelAdmin(admin.ModelAdmin):
	
	
	
	class Meta:
		model = Cart

admin.site.register(Cart, CartModelAdmin)