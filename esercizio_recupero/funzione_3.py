# esesrcizio_3:
"""
Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 2, 4, 6, 8, 10, 12, 14
b) 1, 4, 7, 10, 13
c) 30, 25, 20, 15, 10, 5, 0
d) 5, 15, 25, 35, 45
"""
# a
for i in range(2, 15, 2):
    print(i)

# b
for i in range(1, 14, 3):
    print(i)

#  c
for i in range(0,31, 5):
    print(i)


# altro modo
lista = []
for i in range(30, -1, -5):
    lista.append(i)
print(*lista)


    # d
for i in range(5, 50, 10):
    print(i)


