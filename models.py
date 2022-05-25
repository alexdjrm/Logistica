import itertools

# Classe per un Item da spedire
class Item:
  newid = itertools.count()
  
  def __init__(self, descrizione, altezza, larghezza, lunghezza, peso):
    self.id = next(Item.newid)
    self.descrizione = descrizione
    self.altezza = altezza
    self.larghezza = larghezza
    self.lunghezza = lunghezza
    self.peso = peso
    
  def getVolume(self):
    return self.altezza*self.larghezza*self.lunghezza
    
  def __str__(self):
     return "Item "+str(self.id) +": ["+self.descrizione+"] - "+str(self.altezza) +" x "+ str(self.larghezza) +" x "+ str(self.lunghezza) + " peso: "+  str(self.peso)+"Kg"


    
# Classe per un Vettore che porta certi Item
class Vettore:
  newid = itertools.count()
  def __init__(self, maxVolume, maxPeso):
    self.id = next(Item.newid)
    self.maxVolume = maxVolume
    self.maxPeso = maxPeso
    self.currentPeso = 0
    self.listaItem = []

  def addItem(self, item): 
    if self.currentPeso + item.peso <= 500 :
      self.listaItem.append(item)
      self.currentPeso = self.currentPeso + item.peso
    else:  
      print("Peso massimo over")
  
  def printListaItem(self):
    print("Lista degli oggetti nel vettore")
    for elemento in self.listaItem:
      print(elemento)   

  def __str__(self):
    return "Capacità vettore: "+ str(self.maxVolume) + " cm3 "+ str(self.maxPeso)+"kg"