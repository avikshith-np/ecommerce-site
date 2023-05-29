"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings


from core.views import FrontPage
from accounts.views import UserRegistrationView, loginview, logoutrequest
from store.views import cart, add_to_cart, update_cart, remove_from_cart, add_product, edit_product, remove_product


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FrontPage, name='frontpage'),

    path('accounts/register/', UserRegistrationView.as_view(), name='register'),
    path('accounts/login/', loginview, name='login'),
    path('accounts/logout/', logoutrequest, name='logoutrequest'),

    path('cart/', cart, name='cart'),
    path('product/<int:product_id>/add-to-cart/', add_to_cart, name='add_to_cart'),
    
    path('cart/<int:product_id>/update/', update_cart, name='update_cart'),
    path('cart/<int:product_id>/remove/', remove_from_cart, name='remove_from_cart'),

    path('product/add/', add_product, name='add_product'),
    path('product/<int:product_id>/edit/', edit_product, name='edit_product'),
    path('product/<int:product_id>/remove/', remove_product, name='remove_product'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
