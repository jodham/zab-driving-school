from django.shortcuts import render, get_object_or_404
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


# ------------------x-----------CreateView-------x---------->

# -----------------------------updateView------------------>
class VehicleUpdateView(UpdateView):
    model = Vehicle
    fields = ['vehicleId', 'vehicletypeId', 'vehicleModel', 'registrationDetails']

    def form_valid(self, form):
        return super().form_valid()


# ------------------x-----------updateView-------x---------->

# -----------------------------DetailView------------------>
class CustomerDetailView(DetailView):
    model = Customer


class StaffDetailView(DetailView):
    model = Staff
    template_name = 'indexApp/staff_detail.html'


# -----------------------------DetailView------------------>
# -----------------------------deleteView------------------>
class VehicleDeleteView(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicle')

    def get_context_data(self, **kwargs):
        context = super(VehicleDeleteView, self).get_context_data(**kwargs)
        context['something'] = Vehicle.objects.filter(pk=self.kwargs.get('pk'))
        return context
# ------------------x-----------deleteView---------x--------->
