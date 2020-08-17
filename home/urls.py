from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
app_name='home'


urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('contact',contact,name='contact'),
    path('gallery', GalleryView.as_view(), name='gallery'),
    path('book', book,name='book'),
    path('add_to_book',add_to_book, name='add_to_book'),
    path('delete_book/<slug>',delete_book,name="delete_book"),
    path('checkout',checkout,name='checkout'),
    path('add_to_checkout',add_to_checkout,name='add_to_checkout'),
    path('payment',payment,name='payment'),
    path('success',success,name="success"),
]

