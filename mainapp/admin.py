from __future__ import unicode_literals
from django.contrib import admin
from .models import Cards

class CardsModelAdmin(admin.ModelAdmin):
	
	search_fields = ["name"]
	
	class Meta:
		model = Cards

admin.site.register(Cards, CardsModelAdmin)