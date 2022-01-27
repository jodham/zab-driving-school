from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('staff/', StaffListView.as_view(), name='staff')
]
