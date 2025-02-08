import pytest
import math

from api.models import Ambulance, AccidentReport


@pytest.mark.django_db
def test_create_ambulance():
    ambulance = Ambulance.objects.create(
        plate_number="ABC123",
        ambulance_type="BASIC",
        status="available",
        capacity=4,
        last_inspection_date="2023-01-01T00:00:00Z",
        latitude=3.42418550334237,
        longitude=-76.54422769228785,
        address="Cra. 38a #5A 100, Santa Isabel, Cali, Valle del Cauca",
        created_at="2025-02-08T18:55:23.404300Z",
        assigned_hospital=None
    )

    assert ambulance.plate_number == "ABC123"
    assert ambulance.ambulance_type == "BASIC"
    assert ambulance.status == "available"
    assert ambulance.capacity == 4
    assert math.isclose(ambulance.latitude, 3.42418550334237, rel_tol=1e-09, abs_tol=1e-09)
    assert ambulance.longitude == -76.54422769228785
    assert ambulance.address == "Cra. 38a #5A 100, Santa Isabel, Cali, Valle del Cauca"

@pytest.mark.django_db
def test_create_accident_report():
    accident_report = AccidentReport.objects.create(
        accident_time="2025-01-31T18:30:33.150465Z",
        created_at="2025-01-31T18:30:33.150465Z",
        updated_at="2025-01-31T18:30:33.150465Z",
        description="Example",
        is_active=True,
        is_resolved=False,
        resolved_at=None,
        latitude=3.5833956066287675,
        longitude=-76.49551073088583,
        address="Cra. 3A #9-103, Br. Puerto Isaac, Yumbo, Valle del Cauca",
        assigned_ambulance=None,
        severity="BASIC"
    )

    assert accident_report.description == "Example"
    assert accident_report.is_active == True
    assert accident_report.is_resolved == False
    assert math.isclose(accident_report.latitude, 3.5833956066287675, rel_tol=1e-09, abs_tol=1e-09)
    assert accident_report.longitude == -76.49551073088583
    assert accident_report.address == "Cra. 3A #9-103, Br. Puerto Isaac, Yumbo, Valle del Cauca"
    assert accident_report.severity == "BASIC"