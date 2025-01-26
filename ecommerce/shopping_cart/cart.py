from decimal import Decimal
from store.models import Product

# {'session_key': {'4': {'price': '9.99', 'qty': 1}, '5': {'price': '9.99', 'qty': 2}}}


class Cart:
    
    def __init__(self, request) -> None:
        self.session = request.session
        # for existing users
        cart = self.session.get('session_key')  #  session_key just a name of the session, we can call it anything we want.
        # for new users
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {} # create a new session 
        
        self.cart = cart  # save 

    def add(self, product, product_qty):
        product_id = str(product.id)

        if product_id in self.cart:  # product is already in the cart and we only modify the quantity.
            self.cart[product_id]['qty'] = product_qty
        else:  # save product and product quantity.
            self.cart[product_id] = {'price': str(product.price), 'qty': product_qty}
        
        self.session.modified = True  # update session status to save the data. 

    def __len__(self):
        """ To save quantity of items in a cart"""
        return sum(item['qty'] for item in self.cart.values())
    
    def __iter__(self):
        """ Get all the products from the shopping cart"""
        all_product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=all_product_ids)
        
        import copy
        cart = copy.deepcopy(self.cart)  # make a deep copy of a current session

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total'] = item['price'] * item['qty']
            yield item 

    def get_total(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())

    def delete(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

    def update(self, product, qty):
        product_id = str(product)
        product_quantity = qty

        if product_id in self.cart:
            self.cart[product_id]['qty'] = product_quantity

        self.session.modified = True