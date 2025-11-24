from rest_framework import serializers
from .models import Admin, Hospital, Ambulance, Patient, AccidentReport
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class HospitalCreationSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Hospital
        fields = ('user', 'name', 'level', 'classification', 'address', 'phone_number', 'bed_capacity', 'is_available', 'latitude', 'longitude', 'description')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        hospital_group, created = Group.objects.get_or_create(name='Hospital')
        user.groups.add(hospital_group)
        hospital = Hospital.objects.create(user=user, **validated_data)
        return hospital

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