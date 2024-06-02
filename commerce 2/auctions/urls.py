from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("active_listings", views.active_listings, name="active_listings"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("mylisting", views.mylisting, name="mylisting"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("add_listing", views.add_listing, name="add_listing"),
    path('bid/<int:id>/', views.bid_view, name='bid'),
   

]
