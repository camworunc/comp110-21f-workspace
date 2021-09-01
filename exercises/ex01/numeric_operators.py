"""Numeric Operators."""

__author__ = "730405263"

left_side: str = input("Left-hand side: ")
right_side: str = input("Right-hand side: ")
left_number: int = int(left_side)
right_number: int = int(right_side)
operation1: str = str(left_number ** right_number)
operation2: str = str(left_number / right_number)
operation3: str = str(left_number // right_number)
operation4: str = str(left_number % right_number)
print(left_side + " ** " + right_side + " is " + operation1)
print(left_side + " / " + right_side + " is " + operation2) 
print(left_side + " // " + right_side + " is " + operation3)
print(left_side + " % " + right_side + " is " + operation4)