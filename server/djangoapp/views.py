from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
def about(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', context)


# Create a `contact` view to return a static contact page
def contact(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/contact.html', context)

# Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    # Handles POST request
    if request.method == "POST":
        # Get username and password from request.POST dictionary
        username = request.POST['username']
        password = request.POST['psw']
        # Try to check if provide credential can be authenticated
        user = authenticate(username=username, password=password)
        if user is not None:
            # If user is valid, call login method to login current user
            login(request, user)
            return redirect('djangoapp:index')
        else:
            # If not, return to login page again
            return render(request, 'djangoapp/index.html', context)
    else:
        return render(request, 'djangoapp/index.html', context)

# ...

# Create a `logout_request` view to handle sign out request
def logout_request(request): 
    logout(request)
    return redirect('djangoapp:index')

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    return render(request,'djangoapp/registration.html')

# Update the `get_dealerships` view to render the index page with a list of dealerships
def home(request):
        return render(request, 'djangoapp/index.html')


def get_dealer_details(request, dealer_id):
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    reviews = Review.objects.filter(dealer=dealer)
    context = {'dealer': dealer, 'reviews': reviews}
    return render(request, 'dealer_details.html', context)


def add_review(request, dealer_id):
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    if request.method == 'POST':
        review = Review(dealer=dealer, user=request.user)
        review.comment = request.POST.get('comment')
        review.rating = int(request.POST.get('rating'))
        review.pub_date = datetime.now()
        review.save()
        messages.success(request, 'Review added successfully')
        return redirect('dealer_details', dealer_id=dealer.id)
    else:
        return render(request, 'add_review.html', {'dealer': dealer})