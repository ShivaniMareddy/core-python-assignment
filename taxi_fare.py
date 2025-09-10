BASE_FARE = 50
DISTANCE_FARE = 10 
def calculate_fare(distance):
    return BASE_FARE + (DISTANCE_FARE * distance)
trips = [5, 10, 3]
total = 0
for i, dist in enumerate(trips, start=1):
    fare = calculate_fare(dist)
    total += fare
    print(f"Trip {i}: ${fare}")
print(f"Total Fare: ${total}")
