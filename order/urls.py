from django.urls import path, include
from .views import (
    OrderView,
    OrderRUDView,
    AddOnView,
    AddOnRUDView,
    OutfitView,
    OutfitRUDView
    )

urlpatterns = [
    path('order/', OrderView.as_view(), name='order'),
    path('order-RUD/<int:pk>/', OrderRUDView.as_view(), name='order_RUD'),
    path('add-on/', AddOnView.as_view(), name='add_on'),
    path('add-on-RUD/<int:pk>/', AddOnRUDView.as_view(), name='add_on_RUD'),
    path('outfit/', OutfitView.as_view(), name='outfit'),
    path('outfit-RUD/<int:pk>/', OutfitRUDView.as_view(), name='outfit_RUD'),
]
