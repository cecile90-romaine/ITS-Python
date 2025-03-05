# Exercise 2
"""
Write a function check_length(), which takes a string as an argument.
Using if / else, check if the length of the string is bigger, smaller, or equal to 10 characters
"""

def check_length(mystring):
    if len(mystring) > 10:
        print(f"the lengtn of the string  {mystring} is bigger: ")
    elif len(mystring) < 10:
        print(F" the length of the string {mystring} is smaller: ")
    else:
        print(f" the length of the string {mystring} is equal: ")

check_length(12)
check_length(5)
check_length(10)
