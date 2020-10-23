'''
Nome da classe sempre começa com letra maiuscula
#Separação das palavras por letra maiuscula: PokemonDeFogo
#Classe descreve um determinado objeto
#objetos são instanciações dessa classe
#métodos -- Funções no interior das classes
'''
import random


###Classe Abstrata
class Pokemon:
    def __init__(self, especie, lvl = None, nome = None): #Caso os argumentos nome ou lvl não sejam passados, nao teremos erro
        if lvl == None:
            self.lvl = random.randint(1, 10)
        else:
            self.lvl = lvl

        self.especie = especie

        if nome == None:
            self.nome = especie
        else:
            self.nome = nome

        self.ataque = self.lvl + 10
        self.hp = self.lvl + 20
        self.experiencia = 0


    def __str__(self):
        return "{} ({})" .format(self.nome, self.lvl)


    def passar_lvl(self):

        if self.experiencia >= 2*self.lvl + 300:
            self.lvl += 1
            self.experiencia = 0
            print("{} passou de level!!".format(self))
        else:
            pass


    def atacar(self, pokemon):

        b = int(self.ataque * random.uniform(0.5, 1))
        pokemon.hp -= b
        print("{} perdeu {} pontos de vida".format(pokemon, b))

        if pokemon.hp <= 0:
            print("{} foi derrotado".format(pokemon))
            self.passar_lvl()
            return True

        else:
            return False

####Classes filhas-------------------------------------
#Definir classes filhas - - Herda as caracteristicas do pai
#Alguns subtipos de pokemons



class PokemonEletrico(Pokemon):
    tipo = "Eletrico"


    def atacar(self, pokemon,a):

        print("Ataques: ")
        print("1 - Choque do trovao")
        print("2 - Investida trovao")
        if a == True:
            escolher_ataque = int(input("Escolha o ataque:"))
        else:
            escolher_ataque = random.randint(1, 2)

        if escolher_ataque == 1:
            print("{} usou choque do trovao em {}!".format(self.especie, pokemon.especie))
            if (pokemon.tipo == "Agua") :
                 a = int((self.ataque * random.uniform(1, 1.5)))  # Random.uniform retorna n float entre (a,b)
                 pokemon.hp -=a
                 print("{} perdeu {} pontos de vida".format(pokemon, self.ataque))
                 if pokemon.hp <= 0:
                     print("{} foi derrotado".format(pokemon))
                     self.passar_lvl()
                     return True

                 else:
                     return False
            else:
                 return super().atacar(pokemon)
        elif escolher_ataque == 2:
            print("{} investida trovao em {}!".format(self.especie, pokemon.especie))
            if (pokemon.tipo == "Agua"):
                a = int((self.ataque * random.uniform(1, 1.5)))  # Random.uniform retorna n float entre (a,b)
                pokemon.hp -=a
                print("{} perdeu {} pontos de vida".format(pokemon, self.ataque))
                if pokemon.hp <= 0:
                    print("{} foi derrotado".format(pokemon))
                    self.passar_lvl()
                    return True

                else:
                    return False
            else:
                return super().atacar(pokemon)
        else:
            print("Escolha invalida")




class PokemonFogo(Pokemon):
    tipo = "Fogo"


    def atacar(self, pokemon,a):
        print("Ataques: ")
        print("1 - Lança chamas")
        print("2 - Fire punch")
        if a == True:
            escolher_ataque = int(input("Escolha o ataque:"))
        else:
            escolher_ataque = random.randint(1, 2)

        if escolher_ataque == 1:
            print("{} usou lanca chamas em {}!".format(self.especie, pokemon.especie))
            if (pokemon.tipo == "Grama"):
                a = int((self.ataque * random.uniform(1, 1.5)))  # Random.uniform retorna n float entre (a,b)
                pokemon.hp -=a
                print("{} perdeu {} pontos de vida".format(pokemon, self.ataque))
                if pokemon.hp <= 0:
                    print("{} foi derrotado".format(pokemon))
                    self.passar_lvl()
                    return True

                else:
                    return False
            else:
                return super().atacar(pokemon)

        elif escolher_ataque == 2:
            print("{} fire punch em {}!".format(self.especie, pokemon.especie))
            if (pokemon.tipo == "Grama"):
                a = int((self.ataque * random.uniform(1, 1.5)))  # Random.uniform retorna n float entre (a,b)
                pokemon.hp -=a
                print("{} perdeu {} pontos de vida".format(pokemon, self.ataque))
                if pokemon.hp <= 0:
                    print("{} foi derrotado".format(pokemon))
                    self.passar_lvl()
                    return True

                else:
                    return False
            else:
                return super().atacar(pokemon)

        else:
            print("Escolha invalida")


class PokemonAgua(Pokemon):
    tipo = "Agua"


    def atacar(self, pokemon,a):
        print("Ataques: ")
        print("1 - Jato dagua")
        print("2 - waterfall")
        if a == True:
            escolher_ataque = int(input("Escolha o ataque:"))
        else:
            escolher_ataque = random.randint(1, 2)

        if escolher_ataque == 1:
            print("{} usou jato dagua em {}!".format(self.especie, pokemon.especie))
            if (pokemon.tipo == "Fogo"):
                a = int((self.ataque * random.uniform(1, 1.5)))  # Random.uniform retorna n float entre (a,b)
                pokemon.hp -=a
                print("{} perdeu {} pontos de vida".format(pokemon, self.ataque))
                if pokemon.hp <= 0:
                    print("{} foi derrotado".format(pokemon))
                    self.passar_lvl()
                    return True

                else:
                    return False
            else:
                return super().atacar(pokemon)

        elif escolher_ataque == 2:
            print("{} waterfall em {}!".format(self.especie, pokemon.especie))
            if (pokemon.tipo == "Fogo"):
                a = int((self.ataque * random.uniform(1, 1.5)))  # Random.uniform retorna n float entre (a,b)
                pokemon.hp -=a
                print("{} perdeu {} pontos de vida".format(pokemon, self.ataque))
                if pokemon.hp <= 0:
                    print("{} foi derrotado".format(pokemon))
                    self.passar_lvl()
                    return True

                else:
                    return False
            else:
                return super().atacar(pokemon)

        else:
            print("Escolha invalida")


class PokemonPedra(Pokemon):
    tipo = "Pedra"


    def atacar(self, pokemon,a):
        print("Ataques: ")
        print("1 - rock throw")
        print("2 - cabeçada")
        if a == True:
            escolher_ataque = int(input("Escolha o ataque:"))
        else:
            escolher_ataque = random.randint(1, 2)

        if escolher_ataque == 1:
            print("{} usou rock throw em {}!".format(self.especie, pokemon.especie))
            if (pokemon.tipo == "Voador") or (pokemon.tipo == "Inseto"):
                a = int((self.ataque * random.uniform(1, 1.5)))  # Random.uniform retorna n float entre (a,b)
                pokemon.hp -=a
                print("{} perdeu {} pontos de vida".format(pokemon, self.ataque))
                if pokemon.hp <= 0:
                    print("{} foi derrotado".format(pokemon))
                    self.passar_lvl()
                    return True

                else:
                    return False
            else:
                return super().atacar(pokemon)

        elif escolher_ataque == 2:
            print("{} cabeçada em {}!".format(self.especie, pokemon.especie))
            if (pokemon.tipo == "Voador") or (pokemon.tipo == "Inseto") :
                a = int((self.ataque * random.uniform(1, 1.5)))  # Random.uniform retorna n float entre (a,b)
                pokemon.hp -=a
                print("{} perdeu {} pontos de vida".format(pokemon, self.ataque))
                if pokemon.hp <= 0:
                    print("{} foi derrotado".format(pokemon))
                    self.passar_lvl()
                    return True

                else:
                    return False
            else:
                return super().atacar(pokemon)

        else:
            print("Escolha invalida")


class PokemonVoador(Pokemon):
    tipo = "Voador"


    def atacar(self, pokemon,a):
        print("Ataques: ")
        print("1 - asa de aço")
        print("2 - Vendaval")
        if a == True:
            escolher_ataque = int(input("Escolha o ataque:"))
        else:
            escolher_ataque = random.randint(1, 2)

        if escolher_ataque == 1:
            print("{} usou asa de aço em {}!".format(self.especie, pokemon.especie))
            if (pokemon.tipo == "Inseto"):
                a = int((self.ataque * random.uniform(1, 1.5)))  # Random.uniform retorna n float entre (a,b)
                pokemon.hp -=a
                print("{} perdeu {} pontos de vida".format(pokemon, self.ataque))
                if pokemon.hp <= 0:
                    print("{} foi derrotado".format(pokemon))
                    self.passar_lvl()
                    return True

                else:
                    return False
            else:
                return super().atacar(pokemon)

        elif escolher_ataque == 2:
            print("{} vendaval em {}!".format(self.especie, pokemon.especie))
            if (pokemon.tipo == "Inseto"):
                a = int((self.ataque * random.uniform(1, 1.5)))  # Random.uniform retorna n float entre (a,b)
                pokemon.hp -=a
                print("{} perdeu {} pontos de vida".format(pokemon, self.ataque))
                if pokemon.hp <= 0:
                    print("{} foi derrotado".format(pokemon))
                    self.passar_lvl()
                    return True

                else:
                    return False
            else:
                return super().atacar(pokemon)

        else:
            print("Escolha invalida")


class PokemonGrama(Pokemon):
    tipo = "Grama"


    def atacar(self, pokemon,a):
        print("Ataques: ")
        print("1 - folha navalha")
        print("2 - chicote de vinha")
        if a == True:
            escolher_ataque = int(input("Escolha o ataque:"))
        else:
            escolher_ataque = random.randint(1, 2)

        if escolher_ataque == 1:
            print("{} usou folha navalha em {}!".format(self.especie, pokemon.especie))
            if (pokemon.tipo == "Agua"):
                a = int((self.ataque * random.uniform(1, 1.5)))  # Random.uniform retorna n float entre (a,b)
                pokemon.hp -=a
                print("{} perdeu {} pontos de vida".format(pokemon, self.ataque))
                if pokemon.hp <= 0:
                    print("{} foi derrotado".format(pokemon))
                    self.passar_lvl()
                    return True

                else:
                    return False
            else:
                return super().atacar(pokemon)

        elif escolher_ataque == 2:
            print("{} chicote de vinha em {}!".format(self.especie, pokemon.especie))
            if (pokemon.tipo == "Agua"):
                a = int((self.ataque * random.uniform(1, 1.5)))  # Random.uniform retorna n float entre (a,b)
                pokemon.hp -=a
                print("{} perdeu {} pontos de vida".format(pokemon, self.ataque))
                if pokemon.hp <= 0:
                    print("{} foi derrotado".format(pokemon))
                    self.passar_lvl()
                    return True

                else:
                    return False
            else:
                return super().atacar(pokemon)

        else:
            print("Escolha invalida")


class PokemonInseto(Pokemon):
    tipo = "Inseto"


    def atacar(self, pokemon,a):

        print("Ataques: ")
        print("1 - Envenenar")
        print("2 - ataque rapido")
        if a == True:
            escolher_ataque = int(input("Escolha o ataque:"))
        else:
            escolher_ataque = random.randint(1,2)

        if escolher_ataque == 1:
            print("{} usou envenenar em {}!".format(self.especie, pokemon.especie))

            return super().atacar(pokemon)

        elif escolher_ataque == 2:
            print("{} usou ataque rapido em {}!".format(self.especie, pokemon.especie))
            return super().atacar(pokemon)

        else:
            print("Escolha invalida")


