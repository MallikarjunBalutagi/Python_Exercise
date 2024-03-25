def get_username():
    name = input("Enter the name: ")
    return name
def say_hello(name):
    print("Hello", name)
def main():
    name = get_username()
    say_hello(name)
main()
