  
from django.conf.urls import url
from .views import view_cart, add_to_cart, delete_from_cart

"""Url for the cart app"""

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^delete/(?P<id>\d+)', delete_from_cart, name='delete_from_cart'),
]