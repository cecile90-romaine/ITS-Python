from persona import Persona
from alieno import Alieno

# creare un oggetto P  della classe Persona

P:Persona = Persona("Cecile", "Mbazoa", 30)

# visualizzare le informazione relative alla persona
print(P)

#creare un oggetto della classe Alieno


et:Alieno = Alieno("andromeda")

# visualizzare le informazione relative all' Alieno et
print(et)
# l'oggeto  P  invoca il metodo speak()
P.speak()

#l oggetto et invoca il methodo speak()
et.speak()