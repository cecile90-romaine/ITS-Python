#Using RegEx in Python

import re
text: str = " My email is marco@gmail.com"
result:list[str] = re.findall(r'\S+@\S+', text)
print(result)

# Examples/1

import re
text:str = "Rome Paris"
result = re.match(r'[A-Z][a-z]+', text)
print(result.group())


# Example/2

import re

pattern = r'^-?\d+$'
match = re.match(pattern, '123')
print(bool(match)) 


import re
text:str = "I have 20 cats and 3 dogs"
numbers:list[str] = re.findall(r'\d+', text)
print(numbers)