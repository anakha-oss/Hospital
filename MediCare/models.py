from django.db import models

class Appointment(models.Model):

    patient_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    appointment_date = models.DateField()
    appointment_time = models.CharField(max_length=30)
    reason = models.TextField(blank=True)

    def __str__(self):
        return self.patient_name


