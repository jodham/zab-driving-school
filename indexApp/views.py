from django.shortcuts import render, HttpResponseRedirect
from django.template.context_processors import request
from django.urls import reverse_lazy

from .models import *
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView


# -------------------x-----------ListView------------------>


def index(request):
    totalstaff = Staff.objects.all().count()
    totalvehicles = Vehicle.objects.all().count()
    totallessons = Lesson.objects.all().count()
    totalcustomers = Customer.objects.all().count()
    totalrequests = Request.objects.all().count()
    context = {'totalstaff': totalstaff, 'totalvehicles': totalvehicles,
               'totallessons': totallessons, 'totalcustomers': totalcustomers}
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
    context_object_name = 'customer'


class RequestsListView(ListView):
    model = Request
    template_name = 'driveAdmin/request.html'
    context_object_name = 'request'


# -------------------x-----------ListView------------------>


# -----------------------------CreateView------------------>
class VehicleCreateView(CreateView):
    model = Vehicle
    fields = ['vehicletypeId', 'vehicleModel', 'registrationDetails']

    def form_valid(self, form):
        return super().form_valid(form)


class VehicleTypeCreateView(CreateView):
    model = VehicleType
    fields = ['vehicletypeDesc']


class StaffCreateView(CreateView):
    model = Staff
    fields = ['staffId', 'fname', 'lname', 'email', 'mobile', 'job_titleId']

    def form_valid(self, form):
        return super(StaffCreateView, self).form_valid(form)


class JobTitleCreateView(CreateView):
    model = JobTitle
    fields = ['job_titleDesc']


# ------------------x-----------CreateView-------x---------->

# -----------------------------updateView------------------>
class VehicleUpdateView(UpdateView):
    model = Vehicle
    fields = ['vehicletypeId', 'vehicleModel', 'registrationDetails']

    def form_valid(self, form):
        return super(VehicleUpdateView, self).form_valid(form)


class StaffUpdateView(UpdateView):
    model = Staff
    fields = ['staffId', 'fname', 'lname', 'email', 'mobile', 'job_titleId']

    def form_valid(self, form):
        return super(StaffUpdateView, self).form_valid(form)


# ------------------x-----------updateView-------x---------->

# -----------------------------DetailView------------------>
class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'indexApp/customer_detail.html'


class StaffDetailView(DetailView):
    model = Staff
    template_name = 'indexApp/staff_detail.html'


class VehicleDetailView(DetailView):
    model = Vehicle


# -----------------------------DetailView------------------>
# -----------------------------deleteView------------------>
class VehicleDeleteView(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicle')


class StaffDeleteView(DeleteView):
    model = Staff
    success_url = reverse_lazy('staff')
# ------------------x-----------deleteView---------x--------->
