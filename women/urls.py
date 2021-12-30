from django.urls import path, include
from .views import (
    StyleProfileWomenView,
    StyleProfileWomenRUDView,
    WomenSizeView,
    WomenSizeRUDView,
    )

urlpatterns = [
    path('style-profile-men/', StyleProfileWomenView.as_view(), name='style_profile_women'),
    path('style-profile-men-RUD/<int:pk>/', StyleProfileWomenRUDView.as_view(), name='style_profile_women_RUD'),
    path('men-size/', WomenSizeView.as_view(), name='women_size'),
    path('men-size-RUD/<int:pk>/', WomenSizeRUDView.as_view(), name='women_size_RUD'),
]
