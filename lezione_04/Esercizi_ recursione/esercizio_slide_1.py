# esrcizio_slide_1:

"""

Write a Python function called countdown that takes a positive integer n as input 
and prints a countdown from n to zero.
If the input number is negative, display an error message.
To implement the function, you must exclusively use a while loop and the parameter n passed as input to the function.
Declaring any additional variables inside the function is not allowed.
Then, call the function with n = -5 and n = 5


"""
def countdown(n:int) -> None:

    

    if n < 0:
        print(f" error  {n}  could be a positive number")
    while n:
        print(n)
        n = n -1

    else:
        print(" error! inserted number is negative ")
#countdown(-5)
countdown(5)


