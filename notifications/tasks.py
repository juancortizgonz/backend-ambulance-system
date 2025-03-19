from datetime import timedelta
from backend.celery import shared_task
from django.utils.timezone import now
from api.models import Ambulance, AmbulanceDocument

@shared_task
def verificar_documentos():
    today = now().date()
    days_notice = 7 # como .env
    ambulancias = Ambulance.objects.filter(is_active=True)

    for ambulancia in ambulancias:
        documentos_proximos = AmbulanceDocument.objects.filter(
            ambulance=ambulancia,
            expiration_date__lte = today + timedelta(days = days_notice),  # Menos de 7 días para vencer
            expiration_date__gte = today  # Aún no está vencido
        )

        if documentos_proximos.exists():
            asunto = f"🚨 Aviso: Documentos próximos a vencer para {ambulancia.license_plate}"
            mensaje = f"Hola,\n\nLos siguientes documentos de la ambulancia {ambulancia.license_plate} están próximos a vencer:\n\n"
            
            for doc in documentos_proximos:
                mensaje += f"- {doc.document_type.name}: Vence el {doc.expiration_date}\n"

            mensaje += "\nPor favor, renueve los documentos lo antes posible.\n\nSaludos."

            """
            send_mail(
                asunto,
                mensaje,
                "tu_correo@gmail.com",  # Remitente
                [ambulancia.email_contact],  # Destinatario
                fail_silently=False,
            )
            """

            print(f"📧 Correo enviado a {ambulancia.email_contact}")

    return "Verificación y notificación completadas"