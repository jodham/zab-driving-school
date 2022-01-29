from django.shortcuts import render
from .models import *
from django.views.generic import *


# -------------------x-----------ListView------------------>


def index(request):
    totalstaff = Staff.objects.all().count()
    totalvehicles = Vehicle.objects.all().count()
    totallessons = Lesson.objects.all().count()
    totalcustomers = Customer.objects.all().count()
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
    context_object_name = 'customer'


class RequestsListView(ListView):
    model = Request
    template_name = 'driveAdmin/request.html'
    context_object_name = 'request'


# -------------------x-----------ListView------------------>


# -----------------------------CreateView------------------>
class VehicleCreateView(CreateView):
    model = Vehicle
    fields = ['vehicleId', 'vehicletypeId', 'vehicleModel', 'registrationDetails']

    def form_valid(self, form):
        return super().form_valid()


class CustomerCreateView(CreateView):
    model = Customer
    fields = ['customer_id', 'fname', 'lname', 'DOB', 'phone', 'email', 'License_type']

    def form_valid(self, form):
        return super().form_valid()


class StaffCreateView(CreateView):
    model = Staff
    fields = ['vehicleId', 'vehicletypeId', 'vehicleModel', 'registrationDetails']

    def form_valid(self, form):
        return super().form_valid()
# ------------------x-----------CreateView-------x---------->

# -----------------------------updateView------------------>
class VehicleUpdateView(UpdateView):
    model = Vehicle
    fields = ['vehicleId', 'vehicletypeId', 'vehicleModel', 'registrationDetails']

    def form_valid(self, form):
        return super().form_valid()

# ------------------x-----------updateView-------x---------->
