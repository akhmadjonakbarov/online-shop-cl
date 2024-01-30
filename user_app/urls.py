from django.urls import path
from .views import (
    UserLoginView, UserRegisterView, GetUserView,
    UpdateUserView, UpdateUserLocation
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', GetUserView.as_view(), name='user_profile'),
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('update/', UpdateUserView.as_view(), name='user_update'),
    path('update-location/', UpdateUserLocation.as_view(), name='user_location_update')

]
