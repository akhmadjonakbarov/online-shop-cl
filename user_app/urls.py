from django.urls import path
from .views import (
    UserLoginView, UserRegisterView, GetUserView,
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', GetUserView.as_view(), name='user_profile'),
    path('register/', UserRegisterView.as_view(), name='user_register'),

]
