# Create a session for cart


class Cart:

    def __init__(self, request):
        self.session = request.session
        # create new sessions for new users, use existing for returning users.
        cart = self.session.get('session_key')

        if 'session_key' not in self.session:
            # create a new session
            cart = self.session['session_key'] = {}
        self.cart = cart
