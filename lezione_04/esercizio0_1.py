# esercizio_1

""" 
Write a function check_value(), which takes a number as an argument.
Using if / else, the function should print whether the number is bigger, smaller, or equal to 5

"""

def check_value(n):
    
    if n > 5:
        print(f"the number{n} is  bigger then 5: ")
    elif n < 5:
        print(f"the number {n} is  smaller then 5: ")
    else:
        print(f"the number {n} equal to 5: ")

check_value(5)
check_value(10)
check_value(2)