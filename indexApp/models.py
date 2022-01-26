from django.db import models
from django.utils import timezone


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True, max_length=5)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    DOB = models.DateField()
    phone = models.IntegerField(max_length=15)
    email = models.EmailField()
    License_type = models.ForeignKey(LicenseType, on_delete=models.CASCADE)
    is_active = models.CharField(max_length=1)


class Service_type(models.Model):
    servicetypeId = models.IntegerField(primary_key=True, on_delete=models.CASCADE)
    servicetypeDesc = models.CharField(max_length=100)


class Service(models.Model):
    serviceId = models.IntegerField(primary_key=True, max_length=5)
    service_desc = models.TextField()
    service_type_id = models.ForeignKey(Service_type, on_delete=models.CASCADE)
    cost = models.CharField(max_length=5)


class Request(models.Model):
    requestId = models.IntegerField(primary_key=True, max_length=5)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    startDate = models.DateTimeField()
    RequestStatusId = models.ForeignKey(RequestStatus, on_delete=models.CASCADE)
    vehicleTypeId = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    DateCreated = models.DateTimeField(timezone.now)
    Created_by =models.CharField(max_length=25)


class Lesson(models.Model):
    lesson_id = models.IntegerField(primary_key=True)
    lessonTitle = models.CharField(max_length=50)
    cost = models.CharField(max_length=5)
    duration = models.CharField(20)


class Service_lesson(models.Model):
    servicelessonId = models.IntegerField(primary_key=True)
    serviceId = models.ForeignKey(Service, on_delete=models.CASCADE)
    lessson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)


class Reservation_status(models.Model):
    reservationStatusId = models.IntegerField(primary_key=True, max_length=5)
    reservationStatusdesc = models.TextField()
    is_active = models.CharField(max_length=1)


class Reservation(models.Model):
    reservationId = models.IntegerField(primary_key=True, max_length=5)
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


