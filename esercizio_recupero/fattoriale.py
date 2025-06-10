# esercizio fattoriale:

"""
calcola il fattoriale di un numero n

"""

#n!= n * n-1 * n-2.......1
# 5! = 5* 4 * 3 * 2* 1
def fattoriale(n: int) -> int:

    fattoriale: int = 1

    for i in range(n):

        fattoriale *= n - i

    return fattoriale

print(fattoriale(5))


def factoriale(n: int) -> int:

    if n == 1:

        return n
    return factoriale(n - 1) * n


print(fattoriale(5))
