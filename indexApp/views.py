from django.shortcuts import render
from .models import *
from django.views.generic import ListView


def index(request):
    return render(request, 'driveAdmin/adminIndex.html')


class StaffListView(ListView):
    model = Staff
    template_name = 'driveAdmin/staff.html'
    context_object_name = 'staff'