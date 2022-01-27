from django.urls import path
from .views import *

urlpatternsc = [
    path('staff/', StaffListView.as_view(), name='staff')
]
