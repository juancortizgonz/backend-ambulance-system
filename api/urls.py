from django.urls import path
from . import views

urlpatterns = [
    path("admins/", views.AdminList.as_view(), name="admin-list"),
    path("hospitals/", views.HospitalList.as_view(), name="hospital-list"),
    path("patients/", views.PatientList.as_view(), name="patient-list"),

    path("ambulances/", views.AmbulanceList.as_view(), name="ambulance-list"),
    path("ambulances/", views.CreateAmbulance.as_view(), name="ambulance-create"),
    path("ambulances/<int:pk>/", views.AmbulanceDetailUpdateDelete.as_view(), name="ambulance-rud"),
    path("ambulances/accident-reports/<int:accident_report_id>/", views.ListRecommendedAmbulances.as_view(), name="recommended-ambulances"),
    path("ambulances/plate-number/<str:plate_number>/", views.UpdateAmbulancesByPlateNumber.as_view(), name="update-ambulances-by-plate-number"),

    path("accident-reports/", views.ListCreateAccidentReport.as_view(), name="accident-report-list-create"),
    path("accident-reports/<int:pk>/", views.AccidentReportRUD.as_view(), name="accident-report-rud"),
]