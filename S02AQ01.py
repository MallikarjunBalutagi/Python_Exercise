#Using the starting and ending values of your car’s odometer,calculate its mileage

def odometer(start_pt, end_pt, fuel):
    total_distance = end_pt - start_pt
    mileage = total_distance / fuel
    return total_distance, mileage

def get_values():
    start_pt = float(input("Enter the start point: "))
    end_pt = float(input("Enter the end point: "))
    fuel = float(input("Enter the fuel consumed: "))
    return start_pt, end_pt, fuel

start, end, fuel = get_values()
distance, mileage = odometer(start, end, fuel)

print("Total distance traveled:", distance)
print("Mileage:", mileage)
