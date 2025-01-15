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