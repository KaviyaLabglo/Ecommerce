from django.urls import path
from myapp import views
from .views import *

urlpatterns = [
    
  
    #path('',login_page, name= 'login'),
    path('view_page/', views.show_products, name='viewpage'),
    path('home/', product_list.as_view(), name='home'),
    
    path('co/<int:id1>/', views.cart_form, name='addcart'),
    
    path('add/<int:id>/', views.cart_add, name = 'add'),
    path('del_mycart/<int:id>/', views.cart_del, name='cart_delete'),
    #path('logout/',views.logout_user, name='logout'),
    path('qn/<int:id>/', views.cart_update, name = 'quantity'),

    path('mycart/', views.my_cart, name='mycart'),
    path('order/<int:id>/', views.order_table, name='order'),
    path('history/', views.order_history, name = 'history'),
    path('orderdel/<int:id1>/<int:id2>/', views.order_del, name='order_del'),
    
    path('wishlist/<int:id>/', views.add_wish, name="wishlist"),
    path('my_wishlist/', views.my_wishlist, name='mwl'),
    path('del_wl/<int:id>/', views.wishlist_del, name='delwl'),
    
    
   
    
    path('productapi/', productapi.as_view(), name = 'proapi'),
    path('cartapi/', cartapi.as_view(), name = 'cartapi'),
    path('orderapi/', orderapi.as_view(), name='orderapi'),
    path('searchapi/', searchapi.as_view(), name='searchapi'),
    path('success/', views.success, name='success'),
    
    
    
    
    path('create-checkout-session/', views.create_checkout_session, name='checkoutsession'),
   # path('endpoint/', views.endpoint, name='endpoint'),
]
  

