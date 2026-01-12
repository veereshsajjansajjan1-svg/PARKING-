
def calculate_usage_score(num_vehicles, hours):
    total_usage_hours = num_vehicles * hours
    return total_usage_hours


def determine_utilization_status(usage_score):
    if usage_score >= 90:
        return "Over-Utilized Parking Area"
    elif 50 <= usage_score <= 89:
        return "Optimally Utilized Parking Area"
    else:
        return "Under-Utilized Parking Area"

def smart_parking_utilization():
    
    parking_area_name = "Main Campus Parking"
    vehicle_type = "Car"
    number_of_vehicles = 15
    parking_hours = 6

    usage_score = calculate_usage_score(number_of_vehicles, parking_hours)

    utilization_status = determine_utilization_status(usage_score)

    print("---- Parking Utilization Summary ----")
    print(f"Parking Area Name : {parking_area_name}")
    print(f"Vehicle Type      : {vehicle_type}")
    print(f"Number of Vehicles: {number_of_vehicles}")
    print(f"Parking Hours     : {parking_hours}")
    print(f"Usage Score       : {usage_score}")
    print(f"Utilization Status: {utilization_status}")

smart_parking_utilization()
