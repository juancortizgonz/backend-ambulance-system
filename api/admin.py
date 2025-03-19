from django.contrib import admin
from .models import Admin, Hospital, Ambulance, Patient, AccidentReport, DocumentType

admin.site.register(Admin)
admin.site.register(Hospital)
admin.site.register(Ambulance)
admin.site.register(Patient)
admin.site.register(AccidentReport)
admin.site.register(DocumentType)