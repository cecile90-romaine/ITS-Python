class Prodotti:
    def __init__(self, nome, prezzo, disponibilita):
        self.nome = nome
        self.prezzo = prezzo
        self.disponibilita = disponibilita
        
latte = Prodotti("Latte", 2.5, 10)
caffe = Prodotti("Caffe", 5.8, 5)
pasta = Prodotti("Pasta", 0.7, 20)
pomodori = Prodotti("Pomodori", 2, 14)

lista_ptodotti: list = [latte, caffe, pasta, pomodori]

min = lista_ptodotti[0]
max = lista_ptodotti[0]

for i in lista_ptodotti:
    if i.prezzo < min.prezzo:
        min = i
    elif i.prezzo > max.prezzo:
        max = i

print(f"\n{max.nome} è il prodotto piu costoso\n{min.nome} è il prodotto meno costoso\n")
