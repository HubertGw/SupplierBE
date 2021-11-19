from django.contrib import admin
from django.urls import path, include
from offers import views
from products import views
from rest_framework import permissions
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('offers/', include('offers.urls'), name='offer-list'),
    path('products/', include('products.urls'), name='product-list'),

