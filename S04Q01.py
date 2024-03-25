# A Chemical plant has a tank for storing ethanol.When the tank is more than 80% full, it should raise an alarm to close the valve.When the tank is less than 20% full, it
# should send an SMS to buy more liquid.The total tank capacity is 900 litres.Write a program to simulate this.Ask user to enter current level of ethanol in the tank.
# Print the appropriate action based on value entered

def main():
    total_tank_capacity = 900
    current_level = float(input("Enter the tank capacity: "))
    percentage_full = (current_level / total_tank_capacity) * 100

    if percentage_full > 80:
        print("Raise an alarm to close the valve")
    elif percentage_full < 20:
        print("Buy more liquid")
    else:
        print("Current liquid level is within the range")

main()
