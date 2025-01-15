from django.urls import path
from . import views

urlpatterns = [
    path("admins/", views.AdminList.as_view(), name="admin-list"),
    path("hospitals/", views.HospitalList.as_view(), name="hospital-list"),
    path("ambulances/", views.AmbulanceList.as_view(), name="ambulance-list"),
    path("patients/", views.PatientList.as_view(), name="patient-list"),
]