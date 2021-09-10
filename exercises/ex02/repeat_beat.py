"""Repeating a beat in a loop."""
__author__ = "730405263"
# Begin your solution here...

beat: str = input("What beat do you want to repeat? ")
counter: int = int(input("How many times do you want to repeat it? "))
beatrepeat: str = ""

if counter <= 0:
    print("No beat...")
else:
    while counter >= 1:
        beatrepeat = beat + " " + beatrepeat
        counter = counter - 1 
    print(beatrepeat)
