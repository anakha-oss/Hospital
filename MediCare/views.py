from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils import timezone
from .models import Appointment



def login(request):
    if request.method == 'POST':
        return redirect('home')
    return render(request,"login.html")

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")


def contact(request):
    return render(request,"contact.html")



def booking(request):

    if request.method == 'POST':

        patient_name = request.POST.get('patient_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        department = request.POST.get('department')
        doctor = request.POST.get('doctor')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        reason = request.POST.get('reason')

        Appointment.objects.create(
            patient_name=patient_name,
            age=age,
            gender=gender,
            phone=phone,
            email=email,
            department=department,
            doctor=doctor,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            reason=reason
        )

        messages.success(request, 'Appointment booked successfully!')

        return redirect('home')

    return render(request, 'booking.html', {
        'today': timezone.localdate().isoformat()
    })