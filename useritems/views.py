from django.shortcuts import render
from .models import  *
from mainapp.models import Cards


def mycart(request):
	cart ,created = Cart.objects.get_or_create(user=request.user)
	item_id = request.GET.get("item")
	qty = request.GET.get("qty" , 1)

	if item_id:
		cards = Cards.objects.get(id=item_id)
		cart_item,created = CartItem.objects.get_or_create(cart=cart,items=cards)
		if int(qty)<1:
			cart_item.delete()
		else:
			cart_item.quantity = int(qty)
			cart_item.save()




	return render(request, 'cart.html',{'cart': cart})


