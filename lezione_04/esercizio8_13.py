# esercizio8_13 User Profile: 
"""
#  Build a profile of yourself by calling build_profile(), 
# using your first and last names and three other key-value pairs that describe you. 
# All the values must be passed to the function as parameters. 
# The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67" """

def build_profile(first_name: str, last_name: str, **kwargs):
    output = f"{first_name}  {last_name}, "
    for key,value in kwargs.items():
        output += f"{key}, {value}, "
    return output
output = build_profile(" eric", "crow", age=45, hair="brown", weight=72)
print(output)