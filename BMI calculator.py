from time import sleep

def getfloat(question):
    while True:
        try:
            a = float(input(question))
            return a
        except ValueError as e:
            print (f"{e}\n\nPlease enter a number")

def da_thing():
    sleep(1)
    print ("...")
    sleep(1)

name = input("Hey, i\'m gonna help you figure out your bmi but firrst, what\'s your name? ")
da_thing()
height = getfloat(f"Hey {name}, can you tell me your height in cm? ")
da_thing()
weight = getfloat(f"Hey {name}, now just tell me your weight in kgs: ")
da_thing()
print ("Great! Now ill just calculate it")
da_thing()
BMI = weight/(height/100)**2
print (f"Your BMI is {BMI}")
da_thing()
if (BMI < 18):
    print ("That\'s pretty low")
elif (BMI < 24):
    print ("You have a normal BMI")
elif (BMI < 30):
    print ("That\'s a bit high")
else:
    print ("That\'s really high.")
    da_thing()
print ("Bye!")
da_thing()