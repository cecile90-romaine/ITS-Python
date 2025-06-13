# Validazione di Indirizzo IPv4:
import re

def is_valid_ipv4(address: str) -> bool:
    
    modello = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    match = re.match(modello, address)
    if match:                       #            "versione con list comprehension"
        numeri = match.groups()     #  numeri_int: list[int] = [int(i) for i in match.groups()]
        for i in numeri:            #  for i in numeri_int: 
            i = int(i)              #      if i < 0 or i > 255:
            if 0 <= i <=255:        #          return False
                continue
            else:
                return False
    else:
        return False

    return True
    



print(is_valid_ipv4("592.58.02.14"))
    
print(is_valid_ipv4("192.168.0.1"))
print(is_valid_ipv4("256.100.10.1"))
print(is_valid_ipv4("192.168.1"))
print(is_valid_ipv4("192.168.1.a"))



def is_valid_ipv4(address: str) -> bool:

    numeri = address.split('.')
    if len(numeri) != 4:
        return False

    for i in numeri:
        if not i.isdigit():
            return False
        i = int(i)
        if 0 <= i <=255:
            continue
        else:
            return False
        
    return True
