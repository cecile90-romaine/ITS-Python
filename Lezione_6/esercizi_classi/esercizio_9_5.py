# Esercizio9_5: Login Attemps.

"""
Add an attribute called login_attempts to your User class from Exercise 9-3.
Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
Make an instance of the User class and call increment_login_attempts() several times. 
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
 Print login_attempts again to make sure it was reset to 0.
"""
class User:
    def __init__(self, first_name: str, last_name:str,login_attempts:int = 0, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts      #Add an attribute called login_attempts 
        self.kwargs = kwargs
    def describe_user(self):
        print("user profile")
        print(f"user's information is, name:{self.fist_name}, last name: {self.last_name}")
        for k, v in self.kwargs.items():
            print(f"{k},{v}")

    def greet_user(self):       # stampa a personalized greeting
        print(f"good bye! {self.fist_name}, {self.last_name}")
    
    def increment_login_attempts(self):     #the method increment llogin attempts that increment the value of login attempts by 1
        self.login_attempts += 1 
    
    def reset_login_attempts(self):
        self.login_attempts = 0                                                 # resets the value of login attemps to 0


user1 = User("Cecile","Mbazoa",Age ="30",location = "Santa Marinella")          # creazione di istanze User
user1.increment_login_attempts()                                              # chiama piu volte increment_login_attempts
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"the value of login_attempts of the user {user1.first_name} is {user1.login_attempts}")
user1.reset_login_attempts()
print(f"the value of the login_attemps of the user is reset in {user1.login_attempts}")




