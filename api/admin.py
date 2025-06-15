from django.contrib import admin
from .models import Admin, Hospital, Ambulance, Patient, AccidentReport, DocumentType, AmbulanceDocument, Notification
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from rest_framework.authtoken.models import Token

@admin.register(Ambulance)
class AmbulanceAdmin(admin.ModelAdmin):
    def assigned_hospital_name(self, obj):
        return obj.assigned_hospital.name if obj.assigned_hospital else "No asignado"
    assigned_hospital_name.short_description = 'Hospital Asignado'

    list_display = ('plate_number', 'ambulance_type', 'status', 'capacity', 'last_inspection_date', 'assigned_hospital_name')
    search_fields = ('plate_number', 'ambulance_type', 'status')
    list_filter = ('status', 'assigned_hospital')
    ordering = ('-last_inspection_date',)
    inlines = []

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at', 'is_active', 'last_activity')
    search_fields = ('name', 'user__username')
    list_filter = ('is_active',)
    ordering = ('-created_at',)

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'classification', 'address', 'phone_number', 'bed_capacity', 'is_available')
    search_fields = ('name', 'address')
    list_filter = ('level', 'classification', 'is_available')
    ordering = ('-created_at',)

@admin.register(AccidentReport)
class AccidentReportAdmin(admin.ModelAdmin):
    pass

admin.register(Patient)
admin.register(DocumentType)
admin.register(AmbulanceDocument)
admin.register(Notification)

admin.register(User, UserAdmin)
admin.register(Group, GroupAdmin)

admin.register(Token)