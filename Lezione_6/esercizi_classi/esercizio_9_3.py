# Esercizio 9-3. Users:

"""
Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes 
that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. 
Make another method called greet_user() that prints a personalized greeting to the user Create several instances representing different 
users, and call both methods for each user.

"""

class User:
    def __init__(self, first_name: str, last_name:str, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.kwargs = kwargs
    def describe_user(self):
        print("user profile")
        print(f"user's information is, name:{self.fist_name}, last name: {self.last_name}")
        for k, v in self.kwargs.items():
            print(f"{k},{v}")

    def greet_user(self):       # stampa a personalized greeting
        print(f"good bye! {self.fist_name}, {self.last_name}")

        # creazione di altre istanze rapresentanti  altri utenti
    
user1 = User("Cecile","Mbazoa",Age ="30",location="Santa Marinella")
user2 = User("Aliya","Mbazoa",Age="3",location="Santa Marinella")
user3 = User("Achille","solefack",Age="34",location="Civitavecchia")

# chimata method per ogni utente

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()


user3.describe_user()
user3.greet_user()





