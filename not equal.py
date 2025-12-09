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

a = 10
b = 12
c = 12

print (a != b)
print (b != c)
a = "wspeed"
b = "wchat"

if (a != b):
    print (f"{a} and {b} are diffrent")
else:
    print (f"{a} and {b} are the same")

a = getfloat("enter a number")
if (a%2 != 0):
    print (f"{a} is even")
else:
    print (f"{a} is odd")