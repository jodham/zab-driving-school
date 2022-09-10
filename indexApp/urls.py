from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from .views import (StaffListView, StaffCreateView)

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', index, name='index'),

    path('staff/', StaffListView.as_view(), name='staff'),
    path('staff/new/', StaffCreateForm, name='new-staff'),
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
    path('application/new/', ApplicationListView.as_view(), name='new-application'),
    path('application/<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),
    path('application/<int:pk>/delete/', ApplicationDeleteView.as_view(), name='application_delete'),
    path('application/<int:pk>/update', ApplicationUpdateView.as_view(), name='application-update'),

    path('vehicle/', VehicleListView.as_view(), name='vehicle'),
    path('vehicle/add/', VehicleCreateView.as_view(), name='vehicle-create'),
    path('vehicleModel/new/', VehicleTypeCreateView.as_view(), name='vehicletype-create'),
    path('vehicle/<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('vehicle/<int:pk>/delete/', VehicleDeleteView.as_view(), name='vehicle_delete'),
    path('vehicle/<str:pk>/update/', VehicleUpdateView.as_view(), name='vehicle-update'),

    path('newjobtitle/', JobTitleCreateView.as_view(), name='new-job-title'),

    path('accounts/login/', enter, name="login"),
    path('logout/', getout, name="logout"),
    path('register/', signup, name="register"),
    path('profile/', profile, name='profile')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)