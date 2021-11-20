from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from authentication.views import LoginView, RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
