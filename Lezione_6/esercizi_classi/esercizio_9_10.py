# Esercizio9_10: imported Restaurant.

"""
 Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant.
 Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

"""

from Lezione_6.esercizi_classi.esercizio_9_1 import Restaurant

restaurant1 = Restaurant("Special crescioni", "Forlì")
restaurant2 = Restaurant("Cavallucio marino","Italian cuisine") # definizione  di tre istanze restaurante nella classe Restaurant.
restaurant3 = Restaurant("eru", "Camerunian cuisine")
restaurant4 = Restaurant("grillade mullu", "French cuisine" )

restaurant1.describe_restaurant()
restaurant1.open_restaurant()
