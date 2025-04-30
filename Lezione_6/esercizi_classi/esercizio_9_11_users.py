# Esercizio_9_ users:

"""
Create a module users.py containing three classes:

    User: stores first_name, last_name, username, and email; includes describe_user() and greet_user() methods.
    Privileges: holds a list of privileges and a method show_privileges() to display them.
    Admin: stores a User instance and a Privileges instance as attributes.

"""

class User:
    def __init__(self, first_name:str, username:str, email:str):
        self.first_name = first_name
        self.username = username
        self.email = email
    def describe_user(self):
        print(f"name:{self.first_name}, username:{self.username}, email:{self.email} ")
    
    def greet_user(self):
        print(f"Good morning! {self.first_name}")



class Privileges:
    def __init__(self, the_list:list,):
        self.the_list = the_list
        print(f"the list of privileges is {the_list}")
    
    def show_privileges(self, the_list: list):
        self.the_list = the_list
        print(f"the privileges are {the_list}")
        
        

class Admin:
    def __init__(self, user:User, privileges:Privileges):
        self.user = user
        self.privileges = privileges
    def describe_user(self):
        self.user.describe_user()
    def show_privileges(self):
        self.show_privileges()

user = User("Rosa", "Roasali?", "rosaline@gmail.com")

privileges = Privileges(["coppiare", "salvare", "condividere"])
admin = Admin(user, privileges)
user.describe_user()
user.greet_user()

