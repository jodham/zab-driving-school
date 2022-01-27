from django.shortcuts import render
from .models import *
from django.views.generic import ListView


def index(request):
    return render(request, 'driveAdmin/adminIndex.html')


class StaffListView(ListView):
    model = Staff
    template_name = 'driveAdmin/staff.html'
    context_object_name = 'staff'


class VehicleListView(ListView):
    model = Vehicle
    template_name = 'driveAdmin/vehicle.html'
    context_object_name = 'vehicle'


class LessonsListView(ListView):
    model = Lesson
    template_name = 'driveAdmin/lesson.html'
    context_object_name = 'lesson'


class CustomerListView(ListView):
    model = Customer
    template_name = 'driveAdmin/customer.html'
    context_object_name = 'staff'


class RequestsListView(ListView):
    model = Request
    template_name = 'driveAdmin/request.html'
    context_object_name = 'request'