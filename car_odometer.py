#S02Q01:Using the starting and ending values of your car’s odometer, calculate its mileage


start_odometer = int(input("Enter starting odometer reading: "))
end_odometer = int(input("Enter ending odometer reading: "))
fuel_consumed = float(input("Enter fuel consumed (in liters): "))

distance_traveled = end_odometer - start_odometer
mileage = distance_traveled / fuel_consumed

print(f"total distance travelled: {distance_traveled}")
print(f"mileage/litre of car: {mileage}")
