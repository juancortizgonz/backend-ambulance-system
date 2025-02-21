from django.urls import path
from . import views

urlpatterns = [
    path("admins/", views.AdminList.as_view(), name="admin-list"),
    path("hospitals/", views.HospitalList.as_view(), name="hospital-list"),
    path("patients/", views.PatientList.as_view(), name="patient-list"),

    path("ambulances/", views.AmbulanceList.as_view(), name="ambulance-list"),
    path("ambulances/", views.CreateAmbulance.as_view(), name="ambulance-create"),
    path("ambulances/<int:pk>/", views.AmbulanceDetailUpdateDelete.as_view(), name="ambulance-rud"),

    path("accident-reports/", views.ListCreateAccidentReport.as_view(), name="accident-report-list-create"),
    path("accident-reports/<int:pk>/", views.AccidentReportRUD.as_view(), name="accident-report-rud"),
]