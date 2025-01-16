from .serializers import AdminSerializer, HospitalSerializer, AmbulanceSerializer, PatientSerializer, AccidentReportSerializer
from .models import Admin, Hospital, Ambulance, Patient, AccidentReport
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import user_passes_test
from authenticationapi.permissions import CanViewAdmin, CanViewHospital, CanViewAmbulance, CanViewPatient

# We'll use generics.ListAPIView to list all the objects of a model for now
# https://www.django-rest-framework.org/api-guide/generic-views/

class AdminList(generics.ListAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated, CanViewAdmin]


class HospitalList(generics.ListAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = [IsAuthenticated, CanViewHospital]

class AmbulanceList(generics.ListAPIView):
    queryset = Ambulance.objects.all()
    serializer_class = AmbulanceSerializer
    permission_classes = [IsAuthenticated, CanViewAmbulance]

class PatientList(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated, CanViewPatient]

class AccidentReportList(generics.ListAPIView):
    queryset = AccidentReport.objects.all()
    serializer_class = AccidentReportSerializer
    permission_classes = [IsAuthenticated]

class CreateAccidentReport(generics.ListCreateAPIView):
    queryset = AccidentReport.objects.all()
    serializer_class = AccidentReportSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AccidentReportRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccidentReport.objects.all()
    serializer_class = AccidentReportSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)