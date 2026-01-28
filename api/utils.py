import requests
import math
import environ

from .models import Ambulance

env = environ.Env()
environ.Env.read_env()

def get_estimated_time(ambulance_lat, ambulance_long, accident_lat, accident_long, method="distancematrix_ai"):
    if method == "google":
        try:
            response = requests.get(
                "https://maps.googleapis.com/maps/api/distancematrix/json",
                params={
                    "origins": f"{ambulance_lat},{ambulance_long}",
                    "destinations": f"{accident_lat},{accident_long}",
                    "key": env("GOOGLE_DISTANCE_MATRIX_API_KEY")
                }
            )
            response.raise_for_status()
            elements = response.json().get("rows")[0].get("elements")[0]
            if elements.get('status') != 'OK':
                print(f"Error from Google API: {elements.get('status')}")
                return None
            estimated_time_in_secs = elements.get("duration").get("value")
            return math.ceil(estimated_time_in_secs / 60)
        except requests.RequestException as e:
            print(f"Error fetching estimated time from Google: {e}")
            return None
        except (KeyError, IndexError) as e:
            print(f"Error parsing Google Distance Matrix API response: {e}")
            return None

    elif method == "distancematrix_ai":
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
        except (KeyError, IndexError) as e:
            print(f"Error parsing distancematrix.ai API response: {e}")
            return None
    
    else:
        print(f"Invalid ETA method specified: {method}")
        return None

def find_recommended_ambulances(data, eta_method="distancematrix_ai"):
    """
    Finds available ambulances based on accident data and calculates their ETA.
    This function does NOT change the state of any ambulance.
    """
    capacity_required = data.get("people_involved", 1)
    available_ambulances = Ambulance.objects.filter(
        status='available',
        ambulance_type=data.get("severity"),
        capacity__gte=capacity_required
    )
    accident_lat = data.get("latitude")
    accident_long = data.get("longitude")

    ambulances_with_eta = []
    if len(available_ambulances) > 0:
        for ambulance in available_ambulances:
            estimated_time = get_estimated_time(
                ambulance.latitude,
                ambulance.longitude,
                accident_lat,
                accident_long,
                method=eta_method
            )
            if estimated_time is not None:
                ambulances_with_eta.append((ambulance, estimated_time))

        ambulances_with_eta.sort(key=lambda x: x[1])

    return ambulances_with_eta


def assign_ambulance(data, eta_method="distancematrix_ai"):
    """
    Finds recommended ambulances and assigns the closest one to the accident.
    This function CHANGES the status of the closest ambulance to "in_use".
    """
    ambulances_with_eta = find_recommended_ambulances(data, eta_method)

    if ambulances_with_eta:
        closest_ambulance = ambulances_with_eta[0][0]
        closest_ambulance.status = "in_use"
        closest_ambulance.save()

    return ambulances_with_eta