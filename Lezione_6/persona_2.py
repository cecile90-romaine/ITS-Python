class Persona:
    def __init__(self):
        self.name = ""
        self.lastname = ""
        self.age = 0


    def displayData(self) -> None:
        print(f"Nome: {self.name} \nCognome{self.lastname} \nEtà {self.age}")
        
        #funzione che ci consenta di  importare il valore di self.name
    def setName(self, name:str) -> None:
        self.name = name

    #
    def setLastname(self, lastname:str) -> None:
        self.lastname = lastname
        return lastname

    #
    def setAge(self, age:int) -> None:
        if age  < 0 or age > 130:
            self.age = 0
        else:
            self.age = age


     #
    def getName(self) -> str:
        return self.name

    #
    def getLastname(self) -> str:
        return self.lastname
    #
    def getAge(self) -> int:
        return self.age
