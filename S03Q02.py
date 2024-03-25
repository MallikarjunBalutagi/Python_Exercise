#Ask the user to enter a number.If the number is a single digit number,add 7 to it, and print the number in its unit’s place,
#If the number is a two digit number,raise the number to the power of 5, and print the number in its unit’s place
#If the number is a three digit number, ask the user to enter another number. Add the 2 numbers and print the number in its unit’s place

def do_1digit_oper(number):
    if number < 10:
        print("Given number is single digit number:", number + 7)
        
def do_2digit_oper(number):
    if 10 <= number <= 99:
        print("Given number is two digit number:", number ** 5)
        
def do_3digit_oper(number):
    if 100 <= number <= 999:
        num2 = int(input("Enter another number: "))
        print("Given number is three digit number:", number + num2)

def get_number():
    number = int(input("Enter the number: "))
    return number

num1 = get_number()

do_1digit_oper(num1)
do_2digit_oper(num1)
do_3digit_oper(num1)
