from django.contrib import admin
from .models import Category, User, Listing, Bid, Comment, Watchlist

# Registering models with Django Admin
admin.site.register(Category)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Watchlist)

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'starting_bid','id')
    search_fields = ('title','listing_tags__tag')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','id')
    # Customize the display of profile picture data
    def profile_picture_preview(self, obj):
        # You could return a URL or HTML image tag here
        return "Image Preview"
    profile_picture_preview.short_description = 'Profile Picture'

