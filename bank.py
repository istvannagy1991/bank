'''Ez a kis program bekéri a nevet és létrehoz egy virtuális számlát véletlen mennyiségű pénzzel
Ide mi tehetünk be és szedhetünk is ki a számláról
'''

from random import *

class BankSzamla:
    def __init__(self,name = 'Dupont',ertek = 1000):
        self.name = name
        self.ertek = ertek
    
    def betesz(self,osszeg):
        self.ertek +=osszeg
        self.kiir()
    
    def kivesz(self,osszeg):
        self.ertek -=osszeg
        self.kiir()
    
    def kiir(self):
        print(f"{self.name} bankszamlaegyenlege = {self.ertek} euro")   


name = input('Mi a neved?')
penz = randrange(100,1000)
felhasznalo = BankSzamla(name,penz)
felhasznalo.kiir()
while True:
    kerdes = input("Akarsz penzt betenni? y or n")
    if kerdes == 'y':
        be = int(input("Mennyi penzt akarsz betenni?"))
        felhasznalo.betesz(be)
    if kerdes == 'n':
        kerdes = input("Akarsz penzt kivenni? y or n")
        if kerdes == 'y':
            ki = int(input("Mennyi penzt akarsz kivenni?"))
            felhasznalo.kivesz(ki)
        if kerdes == 'n':
            break

felhasznalo.kiir()