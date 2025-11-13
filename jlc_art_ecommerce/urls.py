"""jlc_art_ecommerce URL Configuration"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('home/', include('home.urls')),
    path('products/', include('products.urls')),
    path('custom-artwork-request/', include('custom_artwork_request.urls')),
    path('profiles/', include('profiles.urls')),
    path('', RedirectView.as_view(url='/home/', permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
