#Take 2 numbers from the user.Print which number is a 2 digit number, and which number is a 3 digit number.If it is neither, then print the number as it is

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if 10 <= num1 <= 99:
    print(f"{num1} is a 2 digit number.")
elif 100 <= num1 <= 999:
    print(f"{num1} is a 3 digit number.")
else:
    print(num1)

if 10 <= num2 <= 99:
    print(f"{num2} is a 2 digit number.")
elif 100 <= num2 <= 999:
    print(f"{num2} is a 3 digit number.")
else:
    print(num2)
