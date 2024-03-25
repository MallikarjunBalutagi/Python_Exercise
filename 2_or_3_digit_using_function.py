def perform_check(number):
    if 10 <= number <= 99:
        print("two digit number")
    elif 100 <= number <=999:
        print("three digit number")
    else:
        print(number)
def get_number():
    number = int(input("enter the number: "))
    return number
    
num1 = get_number()
num2 = get_number()

perform_check(num1)
perform_check(num2)
