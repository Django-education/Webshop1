from django.urls import path
<<<<<<< HEAD
from .views import ajax_cart, ajax_cart_display, index, checkout

urlpatterns = [
    path('ajax_cart', ajax_cart),
    path('ajax_cart_display', ajax_cart_display),
    path('checkout', checkout),
    path('', index)
]
=======
from .views import ajax_cart

urlpatterns = [
    path('ajax_cart', ajax_cart)
]
>>>>>>> 9800cbb47d5bb33a0326cecb50d2a383689eee45
