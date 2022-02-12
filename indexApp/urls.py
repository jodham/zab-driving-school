from django.urls import path
from .views import (
    CustomerDetailView,
    index,
    StaffListView,
    StaffDetailView,
    LessonsListView,
    CustomerListView,
    RequestsListView,
    VehicleCreateView,
    VehicleListView,
    VehicleDeleteView,
    VehicleUpdateView
)


urlpatterns = [
    path('', index, name='index'),
    path('staff/', StaffListView.as_view(), name='staff'),
    path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff-detail'),

    path('lesson/', LessonsListView.as_view(), name='lesson'),

    path('customer/', CustomerListView.as_view(), name='customer'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='Customer_detail'),

    path('request/', RequestsListView.as_view(), name='request'),


    path('vehicle/', VehicleListView.as_view(), name='vehicle'),
    path('vehicle/add/', VehicleCreateView.as_view(), name='vehicle-create'),
    path('vehicle/<int:pk>/delete/', VehicleDeleteView.as_view(), name='vehicle_delete'),
    path('vehicle/<str:pk>/update/', VehicleUpdateView.as_view(), name='vehicle-update'),
]
