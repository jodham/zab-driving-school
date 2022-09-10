from abc import ABC

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from .forms import SignupForm, StaffCreateView
from .models import *
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
import random


# from .decorators import allowed_users, admin_only


# @allowed_users(allowed_roles=['admin'])
# @admin_only
def index(request):
    totalstaff = Staff.objects.all().count()
    totalvehicles = Vehicle.objects.all().count()
    totallessons = Lesson.objects.all().count()
    totalcustomers = Student.objects.all().count()
    totalrequests = Application.objects.all().count()
    context = {'totalstaff': totalstaff, 'totalvehicles': totalvehicles,
               'totallessons': totallessons, 'totalcustomers': totalcustomers, 'totalrequests': totalrequests}
    return render(request, 'driveAdmin/adminIndex.html', context)


def home(request):
    return render(request, 'userIndex/index.html')


# @allowed_users(allowed_roles=['admin'])
class StaffListView(ListView):
    model = Staff
    template_name = 'driveAdmin/staff.html'
    context_object_name = 'staff'

    def get_context_data(self, **kwargs):
        context = super(StaffListView, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context


# @allowed_users(allowed_roles=['admin'])
class VehicleListView(ListView):
    model = Vehicle
    template_name = 'driveAdmin/vehicle.html'
    context_object_name = 'vehicle'


# @allowed_users(allowed_roles=['admin'])
class LessonsListView(ListView):
    model = Lesson
    template_name = 'driveAdmin/lesson.html'
    context_object_name = 'lesson'


# @allowed_users(allowed_roles=['admin'])
class CustomerListView(ListView):
    model = Student
    context_object_name = 'student'


# @allowed_users(allowed_roles=['admin'])
class RequestsListView(ListView):
    model = Application
    template_name = 'driveAdmin/request.html'
    context_object_name = 'request'


class ApplicationListView(ListView):
    model = Application
    context_object_name = 'application'


class LicenseTypeListView(ListView):
    model = LicenseType
    context_object_name = 'licenses'
    template_name = 'indexApp/application_form.html'


# -------------------x-----------ListView------------------>


# -----------------------------CreateView------------------>
class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    fields = ['vehicletypeId', 'vehicleModel', 'registrationDetails', 'image']

    def form_valid(self, form):
        return super().form_valid(form)


class VehicleTypeCreateView(LoginRequiredMixin, CreateView):
    model = VehicleType
    fields = ['vehicletypeDesc']


# class StaffCreateView(CreateView):
#     model = Staff
#     fields = ['staffId', 'fname', 'lname', 'email', 'mobile', 'job_titleId']
#
#     def form_valid(self, form):
#         lowercase = "abcdefghijklmnopqrstuvwxyz"
#         uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         number = '0123456789'
#         symbols = "#@&$"
#
#         Use_for = lowercase + uppercase + number + symbols
#         pass_length = 8
#         password = "".join(random.sample(Use_for, pass_length))
#
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#
#         User.objects.create_user(first_name=fname, last_name=lname, email=email)
#         user = authenticate(email=email, pasword=password)
#         return super(StaffCreateView, self).form_valid(form)


def StaffCreateForm(request):
    if request.method == 'POST':
        form = StaffCreateView(request.POST)
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            staffId = request.POST['staffId']
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            phone = request.POST['phone']
            email = request.POST['email']

            group = Group.objects.get(name='staff')
            user.groups.add(group)

            Staff.objects.create(staffId=staffId, fname=fname, lname=lname, phone=phone, email=email)
            return redirect('staff')
    else:
        form = SignupForm()
    return render(request, 'indexApp/staff_form.html', {'form': form})


class JobTitleCreateView(LoginRequiredMixin, CreateView):
    model = JobTitle
    fields = ['job_titleDesc']


class LessonCreateView(LoginRequiredMixin, CreateView):
    model = Lesson
    fields = ['lessonTitle', 'cost', 'duration']

    def form_valid(self, form):
        return super(LessonCreateView, self).form_valid(form)


class ApplicationCreateView(LoginRequiredMixin, CreateView):
    model = Application
    fields = ['license_type']

    def form_valid(self, form):
        form.instance.student_id = self.request.user
        return super(ApplicationCreateView, self).form_valid(form)


# ------------------x-----------CreateView-------x---------->

# -----------------------------updateView------------------>
class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle
    fields = ['vehicletypeId', 'vehicleModel', 'registrationDetails', 'image']

    def form_valid(self, form):
        return super(VehicleUpdateView, self).form_valid(form)


class StaffUpdateView(LoginRequiredMixin, UpdateView):
    model = Staff
    fields = ['staffId', 'fname', 'lname', 'email', 'mobile', 'job_titleId']

    def form_valid(self, form):
        return super(StaffUpdateView, self).form_valid(form)


class ApplicationUpdateView(LoginRequiredMixin, CreateView):
    model = Application
    fields = ['license_type']

    def form_valid(self, form):
        form.instance.student_id = self.request.user
        return super(ApplicationUpdateView, self).form_valid(form)


class LessonUpdateView(LoginRequiredMixin, UpdateView):
    model = Lesson
    fields = ['lessonTitle', 'cost', 'duration']

    def form_valid(self, form):
        return super(LessonUpdateView, self).form_valid(form)


# ------------------x-----------updateView-------x---------->

# -----------------------------DetailView------------------>
class CustomerDetailView(DetailView):
    model = Student
    template_name = 'indexApp/student_detail.html'


class StaffDetailView(DetailView):
    model = Staff
    template_name = 'indexApp/staff_detail.html'


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'indexApp/lesson_detail.html'


class VehicleDetailView(DetailView):
    model = Vehicle


class ApplicationDetailView(DetailView):
    model = Application


# -----------------------------DetailView------------------>
# -----------------------------deleteView------------------>
class VehicleDeleteView(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicle')


class StaffDeleteView(DeleteView):
    model = Staff
    success_url = reverse_lazy('staff')


class ApplicationDeleteView(DeleteView):
    model = Application
    success_url = reverse_lazy('myapplication')


class LessonDeleteView(DeleteView):
    model = Lesson
    success_url = reverse_lazy('lesson')


# ------------------x-----------deleteView---------x--------->
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            phone = request.POST['phone']
            email = request.POST['email']

            group = Group.objects.get(name='student')
            user.groups.add(group)

            Student.objects.create(userid=user, fname=fname, lname=lname, phone=phone, email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'accounts/register.html', {'form': form})


def enter(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect('home')
        error = messages.warning(request, f'wrong credentials check!!')
        templatename = 'accounts/login.html'
        context = {'error': error}
        return render(request, templatename, context)
    templatename = 'accounts/login.html'
    context = {}
    return render(request, templatename, context)


def getout(request):
    logout(request)
    return redirect('home')


def profile(request):
    group = request.user.groups.name
    print(group)
    context = {'group': group}
    return render(request, 'userIndex/profile.html', context)
