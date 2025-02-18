from .serializers import AdminSerializer, HospitalSerializer, AmbulanceSerializer, PatientSerializer, AccidentReportSerializer
from .models import Admin, Hospital, Ambulance, Patient, AccidentReport
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from authenticationapi.permissions import CanViewAdmin, CanViewHospital, CanViewAmbulance, CanViewPatient
from .utils import assign_ambulance

# We'll use generics.ListAPIView to list all the objects of a model for now
# https://www.django-rest-framework.org/api-guide/generic-views/

# Admin operations
class AdminList(generics.ListAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated, CanViewAdmin]

# Hospital operations
class HospitalList(generics.ListAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = [IsAuthenticated, CanViewHospital]

# Ambulance operations
class AmbulanceList(generics.ListAPIView):
    queryset = Ambulance.objects.all()
    serializer_class = AmbulanceSerializer
    permission_classes = [IsAuthenticated, CanViewAmbulance]

class CreateAmbulance(generics.ListCreateAPIView):
    queryset = Ambulance.objects.all()
    serializer_class = AmbulanceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AmbulanceDetailUpdateDelete(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        # This pk is the ambulance's id
        ambulance = Ambulance.objects.get(pk=pk)
        serializer = AmbulanceSerializer(ambulance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        ambulance = Ambulance.objects.get(pk=pk)
        ambulance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        ambulance = Ambulance.objects.get(user=pk)
        serializer = AmbulanceSerializer(ambulance, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        ambulance = Ambulance.objects.get(user=pk)
        serializer = AmbulanceSerializer(ambulance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Patient operations
class PatientList(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated, CanViewPatient]

# Accident Report operations
class ListCreateAccidentReport(generics.ListCreateAPIView):
    queryset = AccidentReport.objects.all()
    serializer_class = AccidentReportSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        assign_ambulance(serializer, self.request.data)

class AccidentReportRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccidentReport.objects.all()
    serializer_class = AccidentReportSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)