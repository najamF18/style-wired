from django.urls import path, include
from .views import (
    InitialProfileDetailView,
    InitialProfileDetailRUDView,
    ExtraTailoredSizeView,
    ExtraTailoredSizeRUDView,
    ShoeCharacteristicView,
    ShoeCharacteristicRUDView,
    PersonalInfoView,
    PersonalInfoRUDView
    )

urlpatterns = [
    path('initial-profile-details/', InitialProfileDetailView.as_view(), name='initial_profile_details'),
    path('initial-profile-details-RUD/<int:pk>/', InitialProfileDetailRUDView.as_view(), name='initial_profile_details_RUD'),
    path('extra-tailored-size/', ExtraTailoredSizeView.as_view(), name='extra_tailored_size'),
    path('extra-tailored-size-RUD/<int:pk>/', ExtraTailoredSizeRUDView.as_view(), name='extra_tailored_size_RUD'),
    path('shoe-characteristic/', ShoeCharacteristicView.as_view(), name='shoe_characteristic'),
    path('shoe-characteristic-RUD/<int:pk>/', ShoeCharacteristicRUDView.as_view(), name='shoe_characteristic_RUD'),
    path('personal-info/', PersonalInfoView.as_view(), name='personal_info'),
    path('personal-info-RUD/<int:pk>/', PersonalInfoRUDView.as_view(), name='personal_info_RUD'),
]
