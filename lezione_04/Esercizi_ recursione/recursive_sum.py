

"""

Write a Python function called recursiveSum that, given an integer n as input, recursively calculates
 the sum of the numbers
from 0 to n.
If the input number n is negative, display an error message and the function must return None.
Then, call the function recursiveSum for n = -5 and n = 5.
Expected Output:
Error! Inserted number is negative!
None
15


"""
def recursive_sum(n:int) -> int:
    if n < 0:        # n is negatif
        print("error! insert number is negative! ")
        return 0
    elif n == 0:        # if n ugual a zoero recursive process must be stopped
        
        return 0
    else:
        return int(n + recursive_sum(n-1))  #  if n is positive, compute recursive_sum 
print(recursive_sum(5))



#Example 2:

def recursiveuminrange(a: int, b: int) -> int:
    if a > b:  # if a > b, scambiamento di valori chiamata temp
        temp:int = a
        a = b #scambio di valore a e b
        b = temp   # a = b
    if b == a:
        return int(a)  # il processo di recursione vienne interrota
    else:
        return int(b + recursiveuminrange(a, b-1))
    
print(recursiveuminrange(5, 10))   # richiamare la funzione a = 5 e b = 10

