from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None)
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    last_activity = models.DateTimeField(blank=True, null=True, auto_now_add=True)

class Hospital(models.Model):
    class Level(models.TextChoices):
        PRIMARY = 'PRIMARY', 'Primary'
        SECONDARY = 'SECONDARY', 'Secondary'
        TERTIARY = 'TERTIARY', 'Tertiary'

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None)
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(
        max_length=255,
        blank=False,
        null=False
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        default=""
    )
    bed_capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    level_of_care = models.CharField(
        max_length=20,
        choices=Level.choices,
        default=Level.PRIMARY
    )
    description = models.TextField(blank=True, default="")

class Ambulance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None)
    plate_number = models.CharField(max_length=20, unique=True)
    ambulance_type = models.CharField(
        max_length=50,
        choices=[('BASIC', 'Basic'), ('UCI', 'UCI')]
    )
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

class Patient(models.Model):
    name = models.CharField(max_length=255)
    ambulance = models.ForeignKey(Ambulance, on_delete=SET_NULL, null=True, blank=True)
    
class AccidentReport(models.Model):
    accident_time = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False)
    description = models.TextField(blank=True, default="")
    is_active = models.BooleanField(default=True)
    is_resolved = models.BooleanField(default=False)
    resolved_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    severity = models.CharField(
        max_length=5,
        choices=[('BASIC', 'Basic'), ('UCI', 'UCI')],
        blank=False,
        default='BASIC'
    )
    latitude = models.DecimalField(max_digits=24, decimal_places=20)
    longitude = models.DecimalField(max_digits=24, decimal_places=20)
    address = models.CharField(max_length=255, blank=False, null=False, default="")
    assigned_ambulance = models.ForeignKey(Ambulance, on_delete=SET_NULL, null=True, blank=True)
    assigned_ambulance_user_id = models.IntegerField(blank=True, null=True)

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

class Notifications(models.Model):
    user = models.ForeignKey(User, on_delete=SET_NULL)
    message = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)