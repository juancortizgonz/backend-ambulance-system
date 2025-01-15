from .serializers import AdminSerializer, HospitalSerializer, AmbulanceSerializer, PatientSerializer
from .models import Admin, Hospital, Ambulance, Patient
from rest_framework import generics

# We'll use generics.ListAPIView to list all the objects of a model for now
# https://www.django-rest-framework.org/api-guide/generic-views/
class AdminList(generics.ListAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    # ToDo: Add custom permission

class HospitalList(generics.ListAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    # ToDo: Add custom permission

class AmbulanceList(generics.ListAPIView):
    queryset = Ambulance.objects.all()
    serializer_class = AmbulanceSerializer
    # ToDo: Add custom permission

class PatientList(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer