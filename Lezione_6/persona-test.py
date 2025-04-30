""" # dal file persona.py importa la classe Persona
from persona import Persona

#creare un oggetto di tipo persona
cm:Persona = Persona("Cecile","Mbazoa", 34)  # si comporta come un costrutore

print(cm)
print(cm.name, cm.lastname, cm.age) """

# dal file persona.py importa la classe Persona

from persona_2 import Persona
# creo una persona
cm:Persona = Persona()


#voglio richiamare la funzione display della classe Persone per stampare in output le informazioni relative alla persona cm
cm.displayData()

# impostare  il nome della persona cm
cm.setName("Cecile")

print("------------")
cm.displayData()

# impostare  il cognome della persona cm
cm.setLastname("Mbazoa")
# impostare l eta della persona cm
cm.setAge(-34)

print("-------")
cm.displayData()



print("------")
print(cm.getName(), cm.getLastname(), cm.getAge())

# provo a chiamare l'oggetto cm come una funzione(prima di aver creato il metodo __call__nella classe Persona)
#cm()# .> output Errore

#provo a chiamare l'oggetto cm come se fosse una funzione (dopo aver creato il metodo__call__nella classe Persona)
cm()

#scriverecm()equivale a richiamare cm. __call__