from django.shortcuts import render
from .models import *
from django.views.generic import ListView


def index(request):
    totalstaff = Staff.objects.all().count()
    totalvehicles = Vehicle.objects.all().count()
    totallessons = Lesson.objects.all().count()
    totalcustomers = Staff.objects.all().count()
    totalrequests = Request.objects.all().count()
    context = {'totalstaff': totalstaff, 'totalvehicles': totalvehicles,
               'totallessons': totallessons, 'totalcustomers': totalcustomers, 'totalrequests': totalrequests}
    return render(request, 'driveAdmin/adminIndex.html', context)


class StaffListView(ListView):
    model = Staff
    template_name = 'driveAdmin/staff.html'
    context_object_name = 'staff'

    def get_context_data(self, **kwargs):
        context = super(StaffListView, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context


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