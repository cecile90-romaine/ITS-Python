
from string import ascii_lowercase, ascii_uppercase

def cifrario_cesare(s: str, key: int):
    lettera = []
    for carattere in s:

        if carattere in ascii_lowercase:
            index = ascii_lowercase.index(carattere)
            new_index = (index + key) % len(ascii_lowercase)
            lettera.append(ascii_lowercase[new_index])
        elif carattere in ascii_uppercase:
            index = ascii_uppercase.index(carattere)
            new_index = (index + key) % len(ascii_lowercase)
            lettera.append(ascii_uppercase[new_index])
        else:
            lettera.append(carattere)
    return ''.join(lettera)

if __name__ == "__main__":
    s = "ciao"
    key = 2
    risultato = (cifrario_cesare("ciao", 28))
    print(risultato)


# corezione:
def cifrario(s: str, k: int) -> str:
    l: str =""

    for carattere in s:    # dobbiamo scorere tutti i carattere. quale è indice associato al carctere?

        if carattere in ascii_lowercase:
           index: int = ascii_lowercase.index(carattere)
           index = (index + k) % len(ascii_lowercase)  #asccii_lowercase è la lista che contiene tutte le lettere

           l += ascii_lowercase[index]
        elif carattere in ascii_lowercase:

            index: int = ascii_uppercase.index(carattere)
            index = (index + k) % len(ascii_lowercase)
            l += ascii_uppercase[index]
        else:
            l += carattere
    return l
s = "ciao"
k = 2
risultato = cifrario(s, k)
print(risultato)

        
