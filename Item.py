from Pokemon import *


class Item:

    def __init__(self,preco = None):

        if preco == None:
            self.preco = 50
        else:
            self.preco = preco


class Potion(Item):

    tipo = "Potion"

    def __str__(self):
        return "{} (${})".format(self.tipo,self.preco)

    def action(self,pokemon):

        pocao = pokemon.lvl +20
        pokemon.hp += pocao



class Revive(Item):
    tipo = "Revive"

    def __str__(self):
        return "{} (${})".format(self.tipo,self.preco)

    def action(self,pokemon):
        auxiliar = 50
        if pokemon.hp<=0:
            pokemon.hp += (auxiliar + (pokemon.lvl)/2)
        else:
            print("Esse pokemon ainda esta vivo")
