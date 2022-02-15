from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


# class adress(models.Model):
#  addressId = models.AutoField()
#  street = models.CharField(max_length=20)
#  city = models.CharField(max_length=20)
# region = models.CharField(max_length=20)
# zipcode = models.IntegerField(max_length=10)

# def __str__(self):
#   return f'{self.city, self.zipcode}'


class JobTitle(models.Model):
    job_titleId = models.AutoField(primary_key=True)
    job_titleDesc = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return f'{self.job_titleDesc}'

    def get_absolute_url(self):
        return reverse('new-staff')


class Staff(models.Model):
    staffId = models.CharField(unique=True, max_length=25)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    email = models.EmailField()
    # addressId = models.ForeignKey(adress, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    job_titleId = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    is_active = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.job_titleId, self.lname}'

    def get_absolute_url(self):
        return reverse('staff-detail', kwargs={'pk': self.pk})


class LicenseType(models.Model):
    licenseTypeId = models.AutoField(primary_key=True)
    licenseTypeDesc = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.licenseTypeDesc}'


class VehicleType(models.Model):
    vehicletypeId = models.AutoField(primary_key=True)
    vehicletypeDesc = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return f'{self.vehicletypeDesc}'

    def get_absolute_url(self):
        return reverse('vehicle-create')


class Vehicle(models.Model):
    vehicletypeId = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicleModel = models.CharField(max_length=30)
    registrationDetails = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.vehicleModel}'

    def get_absolute_url(self):
        return reverse('vehicle-detail', kwargs={'pk': self.pk})


class Customer(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    DOB = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    is_active = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.fname, self.lname}'

    def get_absolute_url(self):
        return reverse('customer-detail', kwargs={'pk': self.pk})


class Service_type(models.Model):
    servicetypeDesc = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.pk}'


class Service(models.Model):
    service_desc = models.TextField()
    service_type_id = models.ForeignKey(Service_type, on_delete=models.CASCADE)
    cost = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.service_type_id}'


class RequestStatus(models.Model):
    requetstatusdesc = models.CharField(max_length=5)
    is_active = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.requetstatusdesc}'


class Application(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    license_type = models.ForeignKey(LicenseType, on_delete=models.CASCADE)
    DateCreated = models.DateTimeField(timezone.now)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.customer_id}'


class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    lessonTitle = models.CharField(max_length=50)
    cost = models.CharField(max_length=5)
    duration = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.lessonTitle}'


class Service_lesson(models.Model):
    serviceId = models.ForeignKey(Service, on_delete=models.CASCADE)
    lessson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.lessson_id}'


class Reservation_status(models.Model):
    reservation_statusId = models.AutoField(primary_key=True)
    reservationStatusdesc = models.TextField()
    is_active = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.is_active}'


class Reservation(models.Model):
    applicationId = models.ForeignKey(Application, on_delete=models.CASCADE)
    vehicleId = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    ServiceLessonId = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    StaffId = models.ForeignKey(Staff, on_delete=models.CASCADE)
    CreatedDate = models.DateTimeField(timezone.now())
    startDate = models.DateTimeField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
