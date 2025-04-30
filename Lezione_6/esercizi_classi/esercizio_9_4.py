# Esercizio9_4:

"""
Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0.
Create an instance called restaurant from this class. Print the number of customers the restaurant has served, 
and then change this value and print it again. Add a method called set_number_served() that lets you set the number of 
customers that have been served. Call this method with a new number and print the value again. 
Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
Call this method with any number you like that could represent how many customers were served in, say, a day of business. 

"""

class Restaurant:
    def __init__(self,restaurant_name:str, cuisine_type:str, number_served: int = 0): # definizione the init method
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):# the method
        print(f"Restaurant name: {self.restaurant_name},Cuisine type: {self.cuisine_type}")
        

    def open_restaurant(self): # the method
        print(f"{self.restaurant_name} is open")

    def set_number_served(self, new_number_served:int = 0):
        self.number_served = new_number_served
        print(f"the numbers of custumers the restaurant {restaurant.restaurant_name} has served is {new_number_served}")

    def increment_number_served(self, valore:int):
        self.number_served += valore
        print(f"the numbers of custumers to the restaurant{restaurant.restaurant_name} has served is increment in {restaurant.number_served}")

 

# ceazione istanze restaurant 2
restaurant= Restaurant("Special crescioni", "Forli", 40) # creazione di un istanza restaurant nella classe Restaurant.

restaurant.number_served = 45                           # cambiamento del valore del numero server

restaurant.set_number_served(5)                            # aggiungi un methodo set number served poi chiama questo metho poi cambia suom valore

restaurant.increment_number_served(14)                      #increment number of server


print(restaurant.restaurant_name)
print(restaurant.cuisine_type)  # stampa individuali attribitti
print(restaurant.number_served)