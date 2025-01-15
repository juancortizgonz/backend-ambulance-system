from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps

# Run this command to create default groups and permissions
# python manage.py create_groups

class Command(BaseCommand):
    help = 'Create default groups and permissions'

    def handle(self, *args, **kwargs):
        groups_permissions = {
            'Admin': [
                'add_user',
                'change_user',
                'delete_user',
                'view_user',
                'add_group',
                'change_group',
                'delete_group',
                'view_group',
                'add_permission',
                'change_permission',
                'delete_permission',
                'view_permission',
                # Ambulances
                'add_ambulance',
                'change_ambulance',
                'delete_ambulance',
                'view_ambulance',
                # Hospitals
                'add_hospital',
                'change_hospital',
                'delete_hospital',
                'view_hospital',
                # Patients
                'add_patient',
                'change_patient',
                'delete_patient',
                'view_patient',
            ],
            'Ambulance': [
                'view_hospital',
                'add_patient',
                'change_patient',
                'delete_patient',
                'view_patient',
                'change_ambulance',
                'view_ambulance',
            ],
            'Hospital': [
                'view_ambulance',
                'add_patient',
                'change_patient',
                'delete_patient',
                'view_patient',
                'change_hospital',
                'view_hospital',
            ],
            'Patient': [
            ],
        }

        for group_name, permissions in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm in permissions:
                permission = Permission.objects.get(codename=perm)
                group.permissions.add(permission)

        self.stdout.write(self.style.SUCCESS('Successfully created custom groups and permissions'))