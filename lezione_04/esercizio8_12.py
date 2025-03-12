# esercizio8_12 Sandwiches: 
"""
# Write a function that accepts a list of items a person wants on a sandwich.
#  The function should have one parameter that collects as many items as the function call provides,
#  and it should print a summary of the sandwich that’s being ordered. 
# Call the function three times, using a different number of arguments each time """

def call_provider(par:list = str):
    for i in par:
        print((i))
par:list = ["hamburger", "chesburger", "dublecheberger", "pomodorro", "bigmac", "patatine"]
print(call_provider(par))
print(call_provider("hambuger", "pomodorro"))
print(call_provider("chesbuger","bigmac"))
print(call_provider("dublechesbuger","patatine"))
