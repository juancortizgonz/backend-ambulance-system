import pytest
from api.utils import assign_ambulance, get_estimated_time
from api.models import Ambulance
from api.serializers import AccidentReportSerializer

@pytest.mark.django_db
def test_assign_ambulance():
    nearest_ambulance = Ambulance.objects.create(
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

    data = {
        "severity": "BASIC",
        "latitude": 3.378358372884709,
        "longitude": -76.53451643976786
    }

    serializer = AccidentReportSerializer(data=data)
    serializer.is_valid()

    assign_ambulance(serializer, data)

    assert serializer.validated_data["assigned_ambulance"] == nearest_ambulance

@pytest.mark.django_db
def test_estimated_time():
    random_ambulance_latitude = 3.42418550334237
    random_ambulance_longitude = -76.54422769228785
    random_accident_latitude = 3.42418550334237
    random_accident_longitude = -76.54422769228785

    estimated_time = get_estimated_time(
        random_ambulance_latitude,
        random_ambulance_longitude,
        random_accident_latitude,
        random_accident_longitude
    )

    assert estimated_time == 0