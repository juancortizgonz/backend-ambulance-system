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

def assign_ambulance(serializer, data):
    available_ambulances = Ambulance.objects.filter(status='available', ambulance_type=data.get("severity"))
    accident_lat = data.get("latitude")
    accident_long = data.get("longitude")

    ambulances_with_time = []

    for ambulance in available_ambulances:
        estimated_time = get_estimated_time(
            ambulance.latitude,
            ambulance.longitude,
            accident_lat,
            accident_long
        )
        ambulances_with_time.append((ambulance, estimated_time))


    ambulances_with_time.sort(key=lambda x: x[1])

    if ambulances_with_time:
        closest_ambulance = ambulances_with_time[0][0]
        serializer.validated_data["assigned_ambulance"] = closest_ambulance

    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)