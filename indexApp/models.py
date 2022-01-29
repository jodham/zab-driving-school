from django.db import models
from django.utils import timezone
from django.urls import reverse


class Address(models.Model):
    addressId = models.AutoField(primary_key=True)
    street = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    zipcode = models.IntegerField()

    def __str__(self):
        return f'{self.city, self.zipcode}'


class JobTitle(models.Model):
    job_titleId = models.AutoField(primary_key=True)
    job_titleDesc = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.job_titleDesc}'


class Staff(models.Model):
    staffId = models.CharField(primary_key=True, max_length=5)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    email = models.EmailField()
    addressId = models.ForeignKey(Address, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    job_titleId = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    is_active = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.job_titleId, self.lname}'


class LicenseType(models.Model):
    licenseTypeId = models.AutoField(primary_key=True)
    licenseTypeDesc = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.licenseTypeDesc}'


class VehicleType(models.Model):
    vehicletypeId = models.AutoField(primary_key=True)
    vehicletypeDesc = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.vehicletypeDesc}'


class Vehicle(models.Model):
    vehicleId = models.AutoField(primary_key=True)
    vehicletypeId = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicleModel = models.CharField(max_length=30)
    registrationDetails = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.vehicleModel}'

    def get_abolute_url(self):
        return reverse('vehicle-update', kwargs={'pk': self.pk})


class Customer(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=5)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    DOB = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    License_type = models.ForeignKey(LicenseType, on_delete=models.CASCADE)
    is_active = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.fname, self.lname}'


class Service_type(models.Model):
    servicetypeId = models.AutoField(primary_key=True)
    servicetypeDesc = models.CharField(max_length=100)


class Service(models.Model):
    serviceId = models.CharField(primary_key=True, max_length=10)
    service_desc = models.TextField()
    service_type_id = models.ForeignKey(Service_type, on_delete=models.CASCADE)
    cost = models.CharField(max_length=5)


class RequestStatus(models.Model):
    requestStatusId = models.AutoField(primary_key=True)
    requetstatusdesc = models.CharField(max_length=5)
    is_active = models.CharField(max_length=3)


class Request(models.Model):
    requestId = models.CharField(primary_key=True, max_length=10)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    startDate = models.DateTimeField()
    RequestStatusId = models.ForeignKey(RequestStatus, on_delete=models.CASCADE)
    vehicleTypeId = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    DateCreated = models.DateTimeField(timezone.now)
    Created_by =models.CharField(max_length=25)


class Lesson(models.Model):
    lesson_id = models.CharField(primary_key=True, max_length=10)
    lessonTitle = models.CharField(max_length=50)
    cost = models.CharField(max_length=5)
    duration = models.CharField(max_length=20)


class Service_lesson(models.Model):
    servicelessonId = models.AutoField(primary_key=True)
    serviceId = models.ForeignKey(Service, on_delete=models.CASCADE)
    lessson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)


class Reservation_status(models.Model):
    reservationStatusId = models.AutoField(primary_key=True)
    reservationStatusdesc = models.TextField()
    is_active = models.CharField(max_length=1)


class Reservation(models.Model):
    reservationId = models.CharField(primary_key=True, max_length=10)
    request_id = models.ForeignKey(Request, on_delete=models.CASCADE)
    Vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    Service_lessonId = models.ForeignKey(Service_lesson, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    lesson_scheduled_date = models.DateTimeField()
    reservation_statusID = models.ForeignKey(Reservation_status, on_delete=models.CASCADE)
    Created_date = models.DateField()
    created_by = models.CharField(max_length=25)
    last_modified_date = models.DateTimeField()
    last_modifiedby = models.CharField(max_length=25)


