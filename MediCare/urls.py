from django.urls import path
from MediCare import views

urlpatterns = [
    path("",views.login,name='login'),
    path("home/",views.home,name='home'),
    path("about/",views.about,name='about'),
    path("contact/",views.contact,name='contact'),
    path("booking/",views.booking,name='booking')
    
]