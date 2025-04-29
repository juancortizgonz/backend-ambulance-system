from datetime import timedelta
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils.timezone import now
from api.models import Ambulance, AmbulanceDocument

@shared_task
def verificar_documentos():
    today = now().date()
    days_notice = 7 # como .env
    ambulancias = Ambulance.objects.all()

    for ambulancia in ambulancias:
        documentos_proximos = AmbulanceDocument.objects.filter(
            ambulance=ambulancia,
            expiration_date__lte = today + timedelta(days = days_notice),  # Menos de 7 días para vencer
            expiration_date__gte = today  # Aún no está vencido
        )

        if documentos_proximos.exists():
            asunto = f"Aviso: Documentos proximos a vencer para {ambulancia.plate_number}"
            mensaje = f"Hola,\n\nLos siguientes documentos de la ambulancia {ambulancia.plate_number} están proximos a vencer:\n\n"
            
            for doc in documentos_proximos:
                mensaje += f"- {doc.document_type.name}: Vence el {doc.expiration_date}\n"

            mensaje += "\nPor favor, renueve los documentos lo antes posible."

            send_mail(
                asunto,
                mensaje,
                settings.EMAIL_HOST_USER,
                [ambulancia.user.email],
                fail_silently=False,
            )

            print(f"Correo enviado a {ambulancia.user.email}")

    return "Verificacion y notificacion completadas"