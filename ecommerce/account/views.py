from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, UpdateUserForm
from django.contrib.auth.models import User

from django.contrib.sites.shortcuts import get_current_site
from . token import user_tokenizer_generate 

from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from payment.forms import ShippingForm
from payment.models import ShippingAddress, Order, OrderItem


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid: 
            user = form.save()  # override the object
            user.is_active = False  # new users accounts are deactivated by default, they need to verify their accounts first
            user.save()

            # email verification setup (template)
            current_site = get_current_site(request)
            subject = 'Account verification email'
            message = render_to_string('account/registration/email-verification.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': user_tokenizer_generate.make_token(user),
                })
            
            user.email_user(subject=subject, message=message)
            
            return redirect('email-verification-sent')  # redirect here after signing up.
        

    
    context = {'form': form}

    return render(request, 'account/registration/register.html', context=context)


def email_verification(request, uidb64, token):
    
    # uid
    unique_id = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=unique_id)

    # success
    if user and user_tokenizer_generate.check_token(user, token):  
        user.is_active = True   
        user.save()
        return redirect('email-verification-success')
    # failed
    else:
        return redirect('email-verification-failed')



def email_verification_sent(request):
    return render(request, 'account/registration/email-verification-sent.html')


def email_verification_success(request):
    return render(request, 'account/registration/email-verification-success.html')



def email_verification_failed(request):
    return render(request, 'account/registration/email-verification-failed.html')


def my_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid(): 
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    context = {'form': form}

    return render(request, 'account/my-login.html', context=context)



def user_logout(request):

    try:
        for key in list(request.session.keys()):
            if key == 'session_key':  # that's what we named our session key in cart.py
                continue  # save the session data. 
            else:
                del request.session[key]  # delete the session when the user is logged out.
    except KeyError:
        pass
    
    messages.success(request, 'Logout success')

    # auth.logout(request)
    return redirect('store')


@login_required(login_url='my-login')
def dashboard(request):
    return render(request, 'account/dashboard.html', {})


@login_required(login_url='my-login')
def profile_management(request):
    
    # Move this from bottom to the very top, so validation happens
    # and existing usernames are not allowed. 
    user_form = UpdateUserForm(instance=request.user)

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.info(request, 'Account updated')
            return redirect('dashboard')
    
    context = {'user_form': user_form}

    return render(request, 'account/profile-management.html', context=context)


@login_required(login_url='my-login')
def delete_account(request):
    user = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        user.delete()
        messages.error(request, 'Account deleted')
        return redirect('store')

    return render(request, 'account/delete-account.html')

# Shipping view
@login_required(login_url='my-login')
def manage_shipping(request):
    try:
        # Account user with shipment information.
        shipping = ShippingAddress.objects.get(user=request.user.id)

    except ShippingAddress.DoesNotExist:  # account user with no shipment information. 
        shipping = None

    form = ShippingForm(instance=shipping)

    if request.method == 'POST':
        form = ShippingForm(request.POST, instance=shipping)
        
        if form.is_valid():
            # assign the user FK 
            shipping_user = form.save(commit=False)
            # add the FK itself
            shipping_user.user = request.user
            shipping_user.save()

            return redirect('dashboard')
        
    return render(request, 'account/manage-shipping.html', {'form': form})


@login_required(login_url='my-login')
def track_orders(request):

    try:
        orders = OrderItem.objects.filter(user=request.user)
        context = {'orders': orders}
        return render(request, 'account/track-orders.html', context=context)
    except:
        return render(request, 'account/track-orders.html', context=context)

    # return render(request, 'account/track-orders.html', {})

