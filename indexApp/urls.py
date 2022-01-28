from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('staff/', StaffListView.as_view(), name='staff'),
    path('lesson/', LessonsListView.as_view(), name='lesson'),
    path('customer/', CustomerListView.as_view(), name='customer'),
    path('request/', RequestsListView.as_view(), name='request'),
    path('vehicle/', VehicleListView.as_view(), name='vehicle'),
]
