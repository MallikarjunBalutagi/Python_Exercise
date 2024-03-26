#Using the starting and ending values of your car’s odometer,and the measure of fuel consumed,calculate the number of stops one should make for refuelling 
#while travelling from Bangalore to Goa,a distance of 560 kms.

def odometer(start_pt, end_pt, fuel, tank_capacity):
    total_distance = end_pt - start_pt
    mileage = total_distance / fuel
    No_of_stop = fuel / tank_capacity
    return total_distance, mileage, No_of_stop

def get_values():
    start_pt = float(input("Enter the start point: "))
    end_pt = float(input("Enter the end point: "))
    fuel = float(input("Enter the fuel consumed: "))
    tank_capacity = float(input("Enter the tank capacity: "))
    return start_pt, end_pt, fuel, tank_capacity

start, end, fuel, tank_capacity = get_values()
total_distance, mileage, No_of_stop = odometer(start, end, fuel, tank_capacity)

print("Total distance traveled:", total_distance)
print("Mileage:", mileage)
print("Number of stops required:", No_of_stop)
