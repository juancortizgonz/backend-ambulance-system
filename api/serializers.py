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
    assigned_ambulance_id = serializers.PrimaryKeyRelatedField(
        queryset=Ambulance.objects.all(),
        source='assigned_ambulance',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = AccidentReport
        fields = '__all__'

    def create(self, validated_data):
        assigned_ambulance = validated_data.pop('assigned_ambulance', None)
        return AccidentReport.objects.create(assigned_ambulance=assigned_ambulance, **validated_data)