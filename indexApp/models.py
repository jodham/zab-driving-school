from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
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
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to="profilepics", null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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
    category = models.CharField(max_length=5, default='staff')
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
    image = models.ImageField(upload_to='images', default='static/images/default.jpg')

    def __str__(self):
        return f'{self.vehicleModel}'

    def get_absolute_url(self):
        return reverse('vehicle-detail', kwargs={'pk': self.pk})

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


from django.utils.dateparse import parse_date

default_date = parse_date('2000-01-01')


class Student(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    category = models.CharField(max_length=8, default='Students')
    DOB = models.DateField(default=default_date, editable=True)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=30, default='Driving')
    email = models.EmailField()
    is_active = models.BooleanField(default=True)

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
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    license_type = models.ForeignKey(LicenseType, on_delete=models.CASCADE)
    DateCreated = models.DateTimeField(timezone.now)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student_id}'


class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    lessonTitle = models.CharField(max_length=50)
    cost = models.CharField(max_length=5)
    duration = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.lessonTitle}'

    def get_absolute_url(self):
        return reverse('lesson-detail', kwargs={'pk': self.pk})


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
