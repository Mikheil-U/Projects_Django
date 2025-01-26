from django.shortcuts import render
from .models import ShippingAddress, Order, OrderItem
from shopping_cart.cart import Cart
from django.http import JsonResponse


def checkout(request):
    # users with account - Pre-fill the form
    if request.user.is_authenticated:
        try:  # authenticated uses with shipping information
            shipping_address = ShippingAddress.objects.get(user=request.user.id)
            context = {'shipping': shipping_address}
            return render(request, 'payment/checkout.html', context=context)
        
        except:
            # authenticated users without the shipping information.
            return render(request, 'payment/checkout.html') 

    # guest users. 
    return render(request, 'payment/checkout.html')


def complete_order(request):
    
    if request.POST.get('action') == 'post':
        name = request.POST.get('name')
        email = request.POST.get('email')

        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')

        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')

        shipping_address = (address1 + "\n" + address2 + "\n" + city + "\n" + state + "\n" + zipcode)

        # shopping cart information
        cart = Cart(request)
        total_cost = cart.get_total()
        '''
            Order variations
            1) Create order -> Account users WITH + WITHOUT shipping the information stored on our website.
            2) Create order -> Guest users without the shipping information
        '''
        if request.user.is_authenticated:
            order = Order.objects.create(full_name=name, email=email, shipping_address=shipping_address, amount_paid=total_cost, user=request.user)
            order_id = order.pk  # save the id of a order after crating it.

            for item in cart:
                OrderItem.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'], price=item['price'], user=request.user)
        else:
            order = Order.objects.create(full_name=name, email=email, shipping_address=shipping_address, amount_paid=total_cost)
            order_id = order.pk  # save the id of a order after crating it.

            for item in cart:
                OrderItem.objects.create(order_id=order_id, product=item['product'], quantity=item['qty'], price=item['price'])
    
    order_success = True
    response = JsonResponse({'success': order_success})

    return response

def payment_success(request):
    # clear the shopping cart after successful checkout.

    for key in list(request.session.keys()):
        if key == 'session_key':   # session_key obtained from shipping_cart/cart.py 
            del request.session[key]  # delete the session.
        

    return render(request, 'payment/payment-success.html', {})


def payment_failed(request):
    return render(request, 'payment/payment-failed.html', {})