from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.core.validators import MaxValueValidator, MinValueValidator

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, default=None)
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    last_activity = models.DateTimeField(blank=True, null=True, auto_now_add=True)

class HospitalOptions:
    level = (
        (1, "First level"),
        (2, "Second level"),
        (3, "Third level")
    )

    admin_classification = (
        (1, "Public"),
        (2, "Private"),
        (3, "Mixed")
    )

class Hospital(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, default=None)
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    level = models.SmallIntegerField(default=1, choices=HospitalOptions.level)
    classification = models.SmallIntegerField(default=1, choices=HospitalOptions.admin_classification)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255, blank=False, null=False, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, default="")
    bed_capacity = models.IntegerField(blank=False, null=False)
    is_available = models.BooleanField(default=True, null=False)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)
    description = models.TextField(blank=True, null=True, default="")

class Ambulance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None)
    plate_number = models.CharField(max_length=20, unique=True)
    ambulance_type = models.CharField(max_length=50, choices=[('BASIC', 'Basic'), ('UCI', 'UCI')])
    status = models.CharField(
        max_length=50,
        choices=[
            ('available', 'Available'),
            ('in_use', 'In use'),
            ('out_of_service', 'Out of service')
        ]
    )
    capacity = models.IntegerField()
    last_inspection_date = models.DateTimeField()
    assigned_hospital = models.ForeignKey(Hospital, on_delete=SET_NULL, null=True, blank=True)
    latitude = models.DecimalField(max_digits=24, decimal_places=20)
    longitude = models.DecimalField(max_digits=24, decimal_places=20)
    address = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add=True)

class PatientOptions:
    sex = (
        ('M', "Male"),
        ('F', "Female")
    )

    status = (
        ('S', "Stable"),
        ('C', "Critical"),
        ('U', "Unconscious")
    )

class Patient(models.Model):
    full_name = models.CharField(max_length=255, default="Nombre no identificado")
    id_number = models.CharField(max_length=16, null=True)
    age = models.IntegerField(null=True)
    sex = models.CharField(choices=PatientOptions.sex, default='M', null=False)
    status = models.CharField(choices=PatientOptions.status, default='S', null=False)
    medical_record = models.CharField(max_length=25, null=True)
    emergency_reason = models.CharField(max_length=255, blank=True, null=True)
    glasgow = models.IntegerField(default=3, validators=[MaxValueValidator(15), MinValueValidator(3)], null=False)
    ambulance = models.ForeignKey(Ambulance, on_delete=SET_NULL, null=True)
    
class AccidentReportOptions:
    severity = (
        ('BASIC', 'Basic'),
        ('UCI', 'UCI')
    )

    type_place = (
        (1, "Public road"),
        (2, "Building"),
        (3, "Institution"),
        (4, "Rural area")
    )

class AccidentReport(models.Model):
    accident_time = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False)
    caller_phone_number = models.CharField(blank=True, null=True, default="")
    description = models.TextField(blank=True, default="")
    is_active = models.BooleanField(default=True)
    is_resolved = models.BooleanField(default=False)
    resolved_at = models.DateTimeField(null=True)
    severity = models.CharField(choices=AccidentReportOptions.severity, default="BASIC", blank=False, null=False)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)
    address = models.CharField(max_length=255, blank=False, null=False, default="")
    reference_point = models.CharField(max_length=255, blank=True, null=True)
    type_place = models.SmallIntegerField(choices=AccidentReportOptions.type_place, default=1)
    people_involved = models.IntegerField(default=1, null=False)
    assigned_ambulance = models.ForeignKey(Ambulance, on_delete=SET_NULL, null=True, blank=True, default=None)
    additional_notes = models.CharField(max_length=255, blank=True, null=True)
    assigned_ambulance_user_id = models.IntegerField(blank=True, null=True, default=None)

class DocumentType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, default="")

class AmbulanceDocument(models.Model):
    ambulance = models.ForeignKey(Ambulance, on_delete=SET_NULL, null=True)
    document_type = models.ForeignKey(DocumentType, on_delete=SET_NULL, null=True)
    document_number = models.CharField(max_length=255)
    issue_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    message = models.TextField(blank=True, default="", null=True)
    created_at = models.DateTimeField(auto_now_add=True)