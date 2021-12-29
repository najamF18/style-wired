from django.urls import path, include
from .views import (
    InitialProfileDetailView,
    InitialProfileDetailRUDView,
    StyleProfileMenView,
    StyleProfileMenRUDView,
    MenSizeView,
    MenSizeRUDView,
    ExtraTailoredSizeView,
    ExtraTailoredSizeRUDView,
    ShoeCharacteristicView,
    ShoeCharacteristicRUDView
    )

urlpatterns = [
    path('initial-profile-details/', InitialProfileDetailView.as_view(), name='initial_profile_details'),
    path('initial-profile-details-RUD/<int:pk>/', InitialProfileDetailRUDView.as_view(), name='initial_profile_details_RUD'),
    path('style-profile-men/', StyleProfileMenView.as_view(), name='style_profile_men'),
    path('style-profile-men-RUD/<int:pk>/', StyleProfileMenRUDView.as_view(), name='style_profile_men_RUD'),
    path('men-size/', MenSizeView.as_view(), name='men_size'),
    path('men-size-RUD/<int:pk>/', MenSizeRUDView.as_view(), name='men_size_RUD'),
    path('extra-tailored-size/', ExtraTailoredSizeView.as_view(), name='extra_tailored_size'),
    path('extra-tailored-size-RUD/<int:pk>/', ExtraTailoredSizeRUDView.as_view(), name='extra_tailored_size_RUD'),
    path('shoe-characteristic/', ShoeCharacteristicView.as_view(), name='shoe_characteristic'),
    path('shoe-characteristic-RUD/<int:pk>/', ShoeCharacteristicRUDView.as_view(), name='shoe_characteristic_RUD'),
]
