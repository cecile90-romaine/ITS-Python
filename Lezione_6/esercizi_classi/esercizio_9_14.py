# Esercizio9_14:Lottery.
"""
Lottery: Create a class LotteryMachine that holds a list containing a series of 10 numbers and 5 letters. 
Implement a method to randomly select 4 items (numbers or letters) from this list to draw a winning ticket. 
Finally, implement a method to display a message saying that any ticket matching the winning 4 items wins a prize.

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
    
    def message_winner(self) -> None:
        print(f"The winning ticket is {self.winning_ticket}")
        print(f"ticket matching with 4 items {self.winning_ticket} wins a prize")




    
lottery = LotteryMachine("lista","winning_ticket")    #create of  istance oa a LotteryMachine
lottery.draw_winning_ticket()                    # Draw the ticket
lottery.message_winner()                         # announce the winner

