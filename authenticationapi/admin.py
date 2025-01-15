from django.contrib import admin
from .models import Admin, Hospital, Ambulance, Patient

admin.site.register(Admin)
admin.site.register(Hospital)
admin.site.register(Ambulance)
admin.site.register(Patient)