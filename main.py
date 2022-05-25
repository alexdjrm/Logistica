from models import *

vett = Vettore(30000,500)

print(vett)

vett.addItem(Item("Vaso",50,20,20,2))
vett.addItem(Item("Pallet",80,120,80,100))
vett.addItem(Item("Cassapanca",100,50,200,100))
vett.printListaItem()

print (vett.currentPeso)