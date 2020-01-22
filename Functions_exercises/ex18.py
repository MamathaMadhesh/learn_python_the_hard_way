# Functions 

def print_two(*args):
    arg1,arg2=args
    print(f"arg1:{arg1} and arg2:{arg2}")


def print_two_again(arg1,arg2):
    print(f"Two arguments {arg1} and {arg2}")

def print_one(arg1):
    print(f"arg1:{arg1}")

def print_none():
    print("No arguments")

print_two('cat','rat')
print_two_again('Lion','tiger')
print_one(24)
print_none()