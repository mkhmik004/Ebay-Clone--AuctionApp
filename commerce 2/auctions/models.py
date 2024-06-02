from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Category(models.Model):
    tag = models.CharField(max_length=100, unique=True,blank=True)

    def __str__(self):
        return self.tag
    
class User(AbstractUser):
     profile_picture= models.URLField(max_length=200, blank=True, null=True)
     
class Listing(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    listing_pic_url=models.URLField(max_length=200, blank=True, null=True)
    starting_bid=models.DecimalField(max_digits=10,decimal_places=2)
    listing_tags=models.ManyToManyField(Category, related_name='listings')
    is_active = models.BooleanField(default=True)
    timestamp=models.DateTimeField(default=timezone.now) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    def __str__(self):
        return f"{self.title} - {self.starting_bid}"
    def current_highest_bid(self):
        highest_bid = self.bids.order_by('-current_bid').first()
        return highest_bid.current_bid if highest_bid else self.starting_bid
    
    
# Bid Model
class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')
    current_bid = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_winning= models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.amount}"
# Comment Model
class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.user} on {self.listing} at {self.timestamp}"
    
# Watchlist Model
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='whatlist')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='watchlist')
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} watching {self.listing}"
