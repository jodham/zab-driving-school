from django.db import models
from django.utils import timezone


class Address(models.Model):
    addressId = models.CharField(primary_key=True, max_length=5)
    street = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    zipcode = models.IntegerField()


class JobTitle(models.Model):
    job_titleId = models.CharField(primary_key=True, max_length=5)
    job_titleDesc = models.CharField(max_length=50)


class Staff(models.Model):
    staffId = models.CharField(primary_key=True, max_length=5)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    email = models.EmailField()
    addressId = models.ForeignKey(Address, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    job_titleId = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    is_active = models.CharField(max_length=3)


class LicenseType(models.Model):
    licenseTypeId = models.CharField(primary_key=True, max_length=5)
    licenseTypeDesc = models.CharField(max_length=100)


class VehicleType(models.Model):
    vehicletypeId = models.CharField(primary_key=True, max_length=10)
    vehicletypeDesc = models.CharField(max_length=50)


class Vehicle(models.Model):
    vehicleId = models.CharField(primary_key=True, max_length=10)
    vehicletypeId = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicleModel = models.CharField(max_length=30)
    registrationDetails = models.CharField(max_length=30)


class Customer(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=5)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    DOB = models.DateField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    License_type = models.ForeignKey(LicenseType, on_delete=models.CASCADE)
    is_active = models.CharField(max_length=1)


class Service_type(models.Model):
    servicetypeId = models.CharField(primary_key=True, max_length=5)
    servicetypeDesc = models.CharField(max_length=100)


class Service(models.Model):
    serviceId = models.CharField(primary_key=True, max_length=5)
    service_desc = models.TextField()
    service_type_id = models.ForeignKey(Service_type, on_delete=models.CASCADE)
    cost = models.CharField(max_length=5)


class RequestStatus(models.Model):
    requestStatusId = models.CharField(primary_key=True, max_length=5)
    requetstatusdesc = models.CharField(max_length=5)
    is_active = models.CharField(max_length=3)


class Request(models.Model):
    requestId = models.CharField(primary_key=True, max_length=5)
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
    servicelessonId = models.CharField(primary_key=True, max_length=10)
    serviceId = models.ForeignKey(Service, on_delete=models.CASCADE)
    lessson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)


class Reservation_status(models.Model):
    reservationStatusId = models.CharField(primary_key=True, max_length=10)
    reservationStatusdesc = models.TextField()
    is_active = models.CharField(max_length=1)


class Reservation(models.Model):
    reservationId = models.CharField(primary_key=True, max_length=5)
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


