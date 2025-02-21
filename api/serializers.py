from rest_framework import serializers
from .models import Admin, Hospital, Ambulance, Patient, AccidentReport

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class AmbulanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambulance
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AccidentReportSerializer(serializers.ModelSerializer):
    assigned_ambulance_user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = AccidentReport
        fields = '__all__'