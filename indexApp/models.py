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
    License_type = models.ForeignKey(LicenseType, on_delete=models.CASCADE)
    is_active = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.fname, self.lname}'

    def get_absolute_url(self):
        return reverse('customer-detail', kwargs={'pk': self.pk})


class Service_type(models.Model):
    servicetypeDesc = models.CharField(max_length=100)


class Service(models.Model):
    service_desc = models.TextField()
    service_type_id = models.ForeignKey(Service_type, on_delete=models.CASCADE)
    cost = models.CharField(max_length=5)


class RequestStatus(models.Model):
    requetstatusdesc = models.CharField(max_length=5)
    is_active = models.CharField(max_length=3)


class Request(models.Model):
    requestId = models.CharField(primary_key=True, max_length=10)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    startDate = models.DateTimeField()
    vehicleTypeId = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    DateCreated = models.DateTimeField(timezone.now)
    Created_by = models.CharField(max_length=25)


class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    lessonTitle = models.CharField(max_length=50)
    cost = models.CharField(max_length=5)
    duration = models.CharField(max_length=20)


class Service_lesson(models.Model):
    serviceId = models.ForeignKey(Service, on_delete=models.CASCADE)
    lessson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)


class Reservation_status(models.Model):
    reservation_statusId = models.AutoField(primary_key=True)
    reservationStatusdesc = models.TextField()
    is_active = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.is_active}'


class Reservation(models.Model):
    reservationId = models.CharField(unique=True, max_length=10)
    request_id = models.ForeignKey(Request, on_delete=models.CASCADE)
    Vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    Service_lessonId = models.ForeignKey(Service_lesson, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    lesson_scheduled_date = models.DateTimeField()
    Created_date = models.DateField()
    created_by = models.CharField(max_length=25)
    last_modified_date = models.DateTimeField()
    last_modifiedby = models.CharField(max_length=25)
