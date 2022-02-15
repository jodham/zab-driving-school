from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),

    path('staff/', StaffListView.as_view(), name='staff'),
    path('staff/new/', StaffCreateView.as_view(), name='new-staff'),
    path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff-detail'),
    path('staff/<int:pk>/update/', StaffUpdateView.as_view(), name='staff-update'),
    path('staff/<int:pk>/delete/', StaffDeleteView.as_view(), name='staff-delete'),

    path('lesson/', LessonsListView.as_view(), name='lesson'),

    path('customer/', CustomerListView.as_view(), name='customer'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),

    path('application/', RequestsListView.as_view(), name='request'),
    path('jobtitle/new/', JobTitleCreateView.as_view(), name='new-JobTitle'),

    path('vehicle/', VehicleListView.as_view(), name='vehicle'),
    path('vehicle/add/', VehicleCreateView.as_view(), name='vehicle-create'),
    path('vehicleModel/new/', VehicleTypeCreateView.as_view(), name='vehicletype-create'),
    path('vehicle/<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('vehicle/<int:pk>/delete/', VehicleDeleteView.as_view(), name='vehicle_delete'),
    path('vehicle/<str:pk>/update/', VehicleUpdateView.as_view(), name='vehicle-update'),

    path('register/', register, name="register")
]
