from django.shortcuts import render
from django.views.generic import *
from drivingschool.indexApp.models import Staff


def index(request):
    return render(request, 'driveAdmin/adminIndex.html')


class StaffListView(ListView):
    model = Staff
    template_name = 'driveAdmin/staff.html'
    context_object_name = 'staff'
