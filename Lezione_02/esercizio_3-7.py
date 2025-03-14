# esercizio3_7 shrinking guest list:
"""
start with ex3_6
Shrinking Guest List: You just found out that your new dinner table 
won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message 
saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain 
in your list. Each time you pop a name from your list, print a message to that person 
letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know 
they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list.
 Print your list to make sure you actually have an empty list at the end of your program. """


Guest_list:list =["elena", "achille", "bianca", "ginevra"]
Guest_list.insert(len(Guest_list), "cecile")

Guest_list.extend(["michelle", "rosa"])
print(*Guest_list)
print("sorry i can invite only two people for dinner: ")

for i in Guest_list[2]:
    print(f"sorry {Guest_list[len(Guest_list)- 1]} i can not invite you for dinner")
    Guest_list.pop()
    print(f"list:{Guest_list}")

for i in Guest_list:
    print(f"{i} would you come to dinner? ")
del Guest_list[-1]
print(f"list:{Guest_list}")
