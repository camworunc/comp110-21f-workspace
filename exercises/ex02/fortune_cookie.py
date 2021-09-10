"""Program that outputs one of at least four random, good fortunes."""
from random import randint
__author__ = "730405263"
# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 

print("Your fortune cookie says... ")

integer: int = randint(1, 4)


if (integer == 1): 
    print("You are going to have a wonderful day today! ")
if (integer == 2): 
    print("Someone great will come into your life very soon! ")
if (integer == 3):
    print("You are going to get a great grade on this assignment! ")
if (integer == 4): 
    print("You are loved by many! ")

print("Now, go spread positive vibes! ")