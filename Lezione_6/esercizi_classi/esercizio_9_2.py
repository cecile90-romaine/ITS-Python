# esercizio9-2:Three Restaurants.

"""
Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() 
for each instance.

"""

from Lezione_6.esercizi_classi.esercizio_9_1 import Restaurant

restaurant1 = Restaurant("Cavallucio marino","Italian cuisine") # definizione  di tre istanze restaurante nella classe Restaurant.
restaurant2 = Restaurant("eru", "Camerunian cuisine")
restaurant3 = Restaurant("grillade mullu", "French cuisine" )

# chiamare il method describe_restaurant per ogni istanza

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()