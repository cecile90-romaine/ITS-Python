# esercizio_2:

"""

Write a class called Student with the attributes name (str) and
studyProgram (str)
2. Create three instances. One for yourself, one for your left neighbour and one
for our right neighbour.
3. Add a method printInfo that prints the name and studyProgram of a
Student. Test your method on the objects!
4. Modify the code and add age and gender to the attributes. Modify your
printing methods respectively too.


"""
class Student:                                     # 1.crezione class studente
    def __init__(self, name:str, studyProgram:str, age:int, gender:int):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender
    def printInfo(self):
        print(f"name: {self.name}, studyProgram: {self.studyProgram}, age: {self.age}, gender: {self.gender}")
        
cecile = Student("cecile", "Data Analys", 34, "Femmina")          # 2.creazione di 3 istanze.
achille = Student("achille", "cyber security", 37, "Maschille")
aliya = Student("aliya", "Automation", 2, "Femmina")

cecile.printInfo()        # 3.Abbiamo aggiunto il methodo printInfo che stampa gli info degli studenti
achille.printInfo()
aliya.printInfo()


 
