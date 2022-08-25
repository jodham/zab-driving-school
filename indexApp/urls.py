from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', index, name='index'),  # admin dashboard
    path('', home, name='home'),  # site landing page

    path('staff/', StaffListView.as_view(), name='staff'),
    path('staff/new/', StaffCreateView.as_view(), name='new-staff'),
    path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff-detail'),
    path('staff/<int:pk>/update/', StaffUpdateView.as_view(), name='staff-update'),
    path('staff/<int:pk>/delete/', StaffDeleteView.as_view(), name='staff-delete'),

    path('lesson/', LessonsListView.as_view(), name='lesson'),
    path('lesson/new/', LessonCreateView.as_view(), name='new_lesson'),
    path('lesson/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('lesson/<str:pk>/update/', LessonUpdateView.as_view(), name='lesson-update'),
    path('lesson/<int:pk>/delete/', LessonDeleteView.as_view(), name='lesson-delete'),

    path('customer/', CustomerListView.as_view(), name='customer'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),

    path('application/', RequestsListView.as_view(), name='request'),
    path('application/new/', ApplicationCreateView.as_view(), name='new-application'),
    path('myapplication/', ApplicationListView.as_view(), name='myapplication'),


    path('vehicle/', VehicleListView.as_view(), name='vehicle'),
    path('vehicle/add/', VehicleCreateView.as_view(), name='vehicle-create'),
    path('vehicleModel/new/', VehicleTypeCreateView.as_view(), name='vehicletype-create'),
    path('vehicle/<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('vehicle/<int:pk>/delete/', VehicleDeleteView.as_view(), name='vehicle_delete'),
    path('vehicle/<str:pk>/update/', VehicleUpdateView.as_view(), name='vehicle-update'),

    path('enter/', enter, name="login"),
    path('logout/', getout, name="logout"),
    path('register/', signup, name="register"),
    path('profile/', profile, name='profile')
]
