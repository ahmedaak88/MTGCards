from django.shortcuts import render
from useritems.models import Cart



def allcarts(request):
	carts = Cart.objects.all()
	context = {
	"user": request.user,
	"carts":carts,

	}
	return render(request, 'allcarts.html',context)
