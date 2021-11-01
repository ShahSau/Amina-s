# from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from .views import home

urlpatterns = [
    path('', home, name='api.home'),
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
    path('user/', include('api.user.urls')),
    path('order/', include('api.order.urls')),
    # path('payment/', include('api.payment.urls')),
    #we are not going to use this, we use our own coustom authentication
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth')
]