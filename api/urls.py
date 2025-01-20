from django.urls import path
from . import views

urlpatterns = [
    path("admins/", views.AdminList.as_view(), name="admin-list"),
    path("hospitals/", views.HospitalList.as_view(), name="hospital-list"),
    path("patients/", views.PatientList.as_view(), name="patient-list"),

    path("ambulances/", views.AmbulanceList.as_view(), name="ambulance-list"),
    path("ambulances/", views.CreateAmbulance.as_view(), name="ambulance-create"),
    path("ambulances/<int:pk>/", views.AmbulanceRUD.as_view(), name="ambulance-rud"),

    path("accident-reports/", views.CreateAccidentReport.as_view(), name="accident-report-create"),
    path("accident-reports/", views.AccidentReportList.as_view(), name="accident-report-list"),
    path("accident-reports/<int:pk>/", views.AccidentReportRUD.as_view(), name="accident-report-rud"),
]