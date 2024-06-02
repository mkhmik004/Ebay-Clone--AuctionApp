from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from auctions.models import Category, User, Listing, Bid, Comment, Watchlist
from .forms import ListingForm,CommentForm
from django import forms



def index(request):
    return render(request, "auctions/index.html")

def active_listings(request):
    # Fetch all categories
    categories = Category.objects.filter(listings__is_active=True).distinct()

    # Initialize selected_categories to an empty list
    selected_categories = []

    if request.method == "POST":
        # Get selected category IDs from POST data
        selected_categories = request.POST.getlist('tags')
        # Fetch listings and filter by selected categories if any
        if selected_categories:
            listings = Listing.objects.filter(listing_tags__id__in=selected_categories).order_by('-timestamp').distinct()
        else:
            listings = Listing.objects.all().order_by('-timestamp')
    else:
        # Fetch all listings by default
        listings = Listing.objects.all().order_by('-timestamp')

    return render(request, "auctions/active_listings.html", {
        "listings": listings,
        "categories": categories,
        "selected_categories": selected_categories
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("active_listings"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")





def register(request):
    if request.method == "POST":
        username = request.POST["username"].strip()
        email = request.POST["email"].strip()
        profile_pic=request.POST["Profile_picture"].strip()

        # Ensure password matches confirmation
        password = request.POST["password"] 
        confirmation = request.POST["confirmation"]
        if password != confirmation or not username or not profile_pic :
            return render(request, "auctions/register.html", {
                "message": "Passwords must match, and all fields must be filled out."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.profile_picture = profile_pic
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })

        login(request, user)
        return HttpResponseRedirect(reverse("active_listings"))
    else:
        return render(request, "auctions/register.html")
@login_required
def category(request):
    tags = Category.objects.filter(listings__is_active=True).distinct()
    categories = Category.objects.all()
    return render(request, "auctions/category.html", {
        "categories": categories
    })
@login_required
def mylisting(request):
     if request.method == 'POST':
         pass
     else: 
         user_id = request.user.id
         listings = Listing.objects.filter(user=user_id).order_by('-timestamp')
         return render(request, "auctions/mylisting.html",{ 'listings': listings})
     
@login_required
def watchlist(request):
    watchlist_items = Watchlist.objects.filter(user=request.user, status=True).order_by('-listing__timestamp')
    
    return render(request, 'auctions/watchlist.html', {'watchlist_items': watchlist_items})


@login_required
def bid_view(request, id):
        listing = get_object_or_404(Listing, pk=id)
        lister_id=listing.user.id
        user = request.user
        user_id = request.user.id
        action = request.POST.get('action')
        comments = listing.comments.all()
        watchlist,created = Watchlist.objects.get_or_create(user=user, listing=listing)
        if action == 'bid' and request.method == 'POST':
            # Handle the bidding logic here
            bid_amount=int(request.POST.get('bid_amount'))
            print(listing.current_highest_bid)
            if bid_amount>listing.starting_bid and bid_amount>listing.current_highest_bid() :
                
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                print("must be greater than")
               
        elif action == 'watchlist' and request.method == 'POST':
            
            watchlist.status = not watchlist.status
            watchlist.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        elif action == 'comment' and request.method == 'POST':
            comment_form = CommentForm(request.POST)
            
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = user
                comment.listing = listing
                comment.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        form = CommentForm(request.POST)
        return render(request, 'auctions/bid.html', {'listing': listing,'lister_id':lister_id,'user_id':user_id,'watchlist':watchlist,'comments':comments,'comment_form':form})
            



@login_required
def add_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('active_listings')
    else:
        form = ListingForm()
    return render(request, 'auctions/add_listing.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))