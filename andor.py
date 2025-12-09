from time import sleep

def getfloat(question):
    
    while True:
        try:
            a = float(input(question))
            return a
        except ValueError as e:
            print (e)
            print("")
            print ("Please enter a number")

def da_thing():
    sleep(1)
    print ("...")
    sleep(1)

name = input(f"Hey, i'm gonna help you do stuff with opperators but first, what\'s your name? ")
a = getfloat(f"Hey {name}, can you enter a number? ")
da_thing()
b = getfloat(f"Hey {name}, can you enter a number? ")
da_thing()
c = getfloat(f"Hey {name}, can you enter a number? ")

print ("a != b is {a != b}")
print ("c != b is {c != b}")
a = "wspeed"
b = "wchat"

if (a != b):
    print (f"{a} and {b} are diffrent")
else:
    print (f"{a} and {b} are the same")
da_thing()
a = getfloat("enter a number")
if (a%2 != 0):
    print (f"{a} is even")
else:
    print (f"{a} is odd")
    da_thing()