# Esercizio9_15:
"""
1.Add a method called simulate_until_win(self, my_ticket) that:

    Accepts a ticket (a list of 4 items).
    Repeatedly draws random tickets using the draw_ticket() method.
    Keeps count of how many attempts it takes until a randomly drawn ticket matches my_ticket.
    Returns the number of attempts and the winning ticket.

2. Create a ticket called my_ticket with 4 numbers or letters from the pool.

3. Use the simulate_until_win() method to simulate how many draws it would take for your ticket to win.

4. Print a message showing:

    Your ticket
    The winning ticket
    How many attempts it took to win

"""

from random import choice                                                #import function to randmly select items
class LotteryMachine:                                                        # Create a class LotteryMachine
    def __init__(self,lista:list,winning_ticket:list ) -> None:
        self.lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b","c", "d", "e"]    # initialize the machine with the lista of 10 numbers and letters
        self.winning_ticket= []                                                  # list to hold the winning ticket
    
        
    def draw_winning_ticket(self) -> None:
        while len(self.winning_ticket) < 4:
            lista1:str = choice(self.lista)                        #  #random.choices() permette di sceliere dalla #ista quantita di caratteri richiesti con possibili ripetizioni
                                                        #random.sample() permette di sceliere dalla lista quantita di caratteri richiesti SENZA ripetizioni
            if lista1 not in self.winning_ticket:
                self.winning_ticket.append(lista1)
        return self.winning_ticket
    
    def message_winner(self) -> None:
        print(f"The winning ticket is {self.winning_ticket}")
        print(f"ticket matching with 4 items {self.winning_ticket} wins a prize")
    def simulate_until_win(self, my_ticket:list[str]) -> tuple[int, list[str]]:
    attempts = 0
    while True:
        new_ticket = self.draw_winning_ticket()
        attempts += 1
        if sorted(new_ticket) == sorted(new_ticket):
            return attempts, new_ticket
        # Define a useer ticket
 my_ticket:list[str] = ["3", "a", "7","d"]
        # create the machine and simulate until a win
machine = LotteryMachine()
attempts,winning_ticket = machine
 
simulate_until_win(my_tiket)  

print(f"your ticket:{my_ticket}")  
print(f"Winning ticket:{winning_ticket}")  
print(f"it took {attempts} attempts to win.")
                                  
    




