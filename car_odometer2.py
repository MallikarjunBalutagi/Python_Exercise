#S02Q02:Using the starting and ending values of your car’s odometer,and the measure of fuel consumed,calculate the number of stops one should make for refuelling while travelling from Bangalore to Goa,a distance of 560 kms.
start_odometer = int(input("Enter starting odometer reading: "))
end_odometer = int(input("Enter ending odometer reading: "))
fuel_consumed = float(input("Enter fuel consumed (in liters): "))
tank_capacity = int(input("Enter the capacity of car tank: "))

distance_traveled = end_odometer - start_odometer
mileage = distance_traveled / fuel_consumed
No_of_stop = tank_capacity / mileage

print(f"total distance travelled: {distance_traveled}")
print(f"mileage/litre of car: {mileage}")
print(f"number of stops one should make for refuelling: {No_of_stop}")
