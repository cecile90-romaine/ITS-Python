# esercizio_4
"""
write a function check_each(), which takes a list of numbers as argument.
Using a for loop, iterate through the list.
For each number, print “bigger” if it’s bigger than 5,
 “smaller” if it’s smaller than 5, and “equal” if it’s equal to 5.

"""
def check_each(list_of_num):
    for i in list_of_num:
        if i > 5:
            print(f"the number {i} is bigger than 5: ")
        elif i < 5:
            print(f" the number {i} is smaller than5: ")
        else:
            print(f"the number {i} is egual to ")

check_each( [10, 11, 1])
check_each([1, 2, 3])
check_each([5, 2 ])