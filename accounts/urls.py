from django.urls import path, include
from .views import (
    UserRegistration,
    check,
    )
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('user-registration/', UserRegistration.as_view(), name='user_registration'),
    path('check/', check.as_view(), name='chcek'),
    # JWT auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
