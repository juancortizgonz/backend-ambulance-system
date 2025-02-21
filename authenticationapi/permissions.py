from rest_framework.permissions import BasePermission

# Permissions to perform ListAPIView operations
class CanViewAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.has_perm('api.view_admin'))

class CanViewHospital(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.has_perm('api.view_hospital'))

class CanViewAmbulance(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.has_perm('api.view_ambulance'))

class CanViewPatient(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.has_perm('api.view_patient'))

class CanCreateReadAmbulance(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and (request.user.has_perm('api.add_ambulance') or request.user.has_perm('api.view_ambulance')))

class CanDetailUpdateAmbulance(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and (request.user.has_perm('api.change_ambulance') or request.user.has_perm('api.view_ambulance')))

class CanListCreateAccidentReport(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and (request.user.has_perm('api.add_accidentreport') or request.user.has_perm('api.view_accidentreport')))

class CanReadUpdateDestroyAccidentReport(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and (request.user.has_perm('api.change_accidentreport') or request.user.has_perm('api.view_accidentreport') or request.user.has_perm('api.delete_accidentreport')))