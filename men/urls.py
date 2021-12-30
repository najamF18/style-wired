from django.urls import path, include
from .views import (
    StyleProfileMenView,
    StyleProfileMenRUDView,
    MenSizeView,
    MenSizeRUDView,
    )

urlpatterns = [
    path('style-profile-men/', StyleProfileMenView.as_view(), name='style_profile_men'),
    path('style-profile-men-RUD/<int:pk>/', StyleProfileMenRUDView.as_view(), name='style_profile_men_RUD'),
    path('men-size/', MenSizeView.as_view(), name='men_size'),
    path('men-size-RUD/<int:pk>/', MenSizeRUDView.as_view(), name='men_size_RUD'),
]
