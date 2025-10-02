import requests
import math
import environ

from .models import Ambulance

env = environ.Env()
environ.Env.read_env()

def get_estimated_time(ambulance_lat, ambulance_long, accident_lat, accident_long):
    try:
        response = requests.get(
            "https://api.distancematrix.ai/maps/api/distancematrix/json",
            params={
                "origins": f"{ambulance_lat},{ambulance_long}",
                "destinations": f"{accident_lat},{accident_long}",
                "key": env("DISTANCE_MATRIX_API")
            }
        )
        response.raise_for_status()
        estimated_time_in_secs = response.json().get("rows")[0].get("elements")[0].get("duration").get("value")
        return math.ceil(estimated_time_in_secs / 60)
    except requests.RequestException as e:
        print(f"Error fetching estimated time: {e}")
        return None

def assign_ambulance(data):
    capacity_required = data.get("people_involved", 1)
    available_ambulances = Ambulance.objects.filter(
        status='available',
        ambulance_type=data.get("severity"),
        capacity__gte=capacity_required
    )
    accident_lat = data.get("latitude")
    accident_long = data.get("longitude")

    if len(available_ambulances) > 0:
        ambulances_with_eta = []

        for ambulance in available_ambulances:
            estimated_time = get_estimated_time(
                ambulance.latitude,
                ambulance.longitude,
                accident_lat,
                accident_long
            )
            ambulances_with_eta.append((ambulance, estimated_time))


        ambulances_with_eta.sort(key=lambda x: x[1])

        return ambulances_with_eta
    else:
        return []