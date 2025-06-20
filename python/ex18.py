#The first function is like script with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#ok, that *args is pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#This just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes no argument
def print_none():
    print("I got nothin'.")

print_two("Jatin", "Yogesh")
print_two_again("Vedit", "Anvik")
print_one("First")
print_none()