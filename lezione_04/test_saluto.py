import saluto # abbiamo importato 

saluto.greet("Federico")

import saluto as s # abbiamo cambiato saluto con s
s.greet(" eleonora")

# se voglio importare solo la funzione geert dal modulo saluto ed ignorare il resto del modulo saluto farò:

from saluto import greet
greet("cecile")
from saluto import greet as g
g


def alpha():
    print("executing alpha")

def beta():
    print("executing beta")

def gamma():
    print("print executing alpha")
    beta()


gamma()

"""
output:
Executing gamma,
Esecuting beta,
Executing alpha

ordine di exsecuzione: gamma() -> beta() -> alpha()

ordine di rimossione: alpha() ->beta() -> gamma()

"""
