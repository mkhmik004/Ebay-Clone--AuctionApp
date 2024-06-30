from django import forms
from .models import Listing,Bid,Comment,Category

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ("title", "description", "listing_pic_url", "starting_bid", "listing_tags")
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'listing_pic_url': forms.URLInput(attrs={'class': 'form-control'}),
            'starting_bid': forms.NumberInput(attrs={'class': 'form-control'}),
            'listing_tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    
    class Meta:
            model = Comment
            fields = ['text']
            widgets = {
                'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Enter your comment here...'})
            }

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['current_bid']
        widgets = {
            'current_bid': forms.NumberInput(attrs={'class': 'form-control'})
        }