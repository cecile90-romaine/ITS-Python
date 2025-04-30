# esercizio_1:
"""

Copy the code and print the age of
bob (using the dot notation)
2. Create an if-statement that prints
the name of the oldest of the two
Persons
3. Create three other Persons. Make
a list called people with all 5
Persons.
4. Make a loop that finds and prints
the youngest person’s name

"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
alice = Person("Alice W.",45)
bob = Person("Bob M.",36)

class Person:
    def __unit__(self, name, age):
        self.name = name
        self.age = age

alice = Person("Alice W.", 45)
bob = Person("bob M.", 36)
print(f"\nEta di Bob: {bob.age}")
if alice.age > bob.age:
    print(f"{alice.name} è piu grande" )
elif alice.age < bob.age:
    print(f"{bob.age} è piu grande")
else:
    print("hanno età uguali")

cecile = Person("cecile. M")
achille = Person("achille. S")
aliya = Person("aliya. M")

people:list = [alice, bob, cecile, achille, aliya]
p_min = people[0]
for p in people:
    if p.age < p_min.age:
        p_min = p
print(f"Eta minore:{p_min.name}")
