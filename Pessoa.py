from Pokemon import *  #Importando todos os dados de Pokemon.py para Pessoa.py
from Item import *

##Tem muito nos games: RNG - Random Name Generate
#random.ranint(a,b) - Gera n aleatorio entre a e b
#random.ranchoice(lista) - escolhe randomicamente um elemento do interior da lista
#random.uniform(a,b) - retorna float entre a e b
#lista[]

NOMES = ["May", "Gary", "andy", "Clark", "Misty", "Ane", "Marie", "Rick"]
POKEMONS = [PokemonAgua("Squirtle"),
            PokemonAgua("Lapras"),
            PokemonFogo("Charmander"),
            PokemonFogo("Arcanine"),
            PokemonEletrico("Pikachu"),
            PokemonEletrico("Electabuzz"),
            PokemonInseto("Beedrill"),
            PokemonInseto("Butterfree"),
            PokemonGrama("Bulbassaur"),
            PokemonGrama("Gloom"),
            PokemonPedra("Onix"),
            PokemonPedra("Rhyhorn"),
            PokemonVoador("Pidgeot"),
            PokemonVoador("Spearow")
            ]


class Pessoa: #Classe mais geral


    def __init__(self, nome=None, pokemons=[], dinheiro=100,itens = []): #inicializando -> passagem dos argumentos

        if nome == None:
            self.nome = random.choice(NOMES) #argumento nome não é obrigatorio
        else:
            self.nome = nome

        self.pokemons = pokemons
        self.dinheiro = dinheiro
        if itens == []:
            self.itens = []
        else:
            self.itens = itens


    def mostrar_pokemons(self,a): #Método para mostrar os pokemons que possuo
        if self.pokemons:
            print("Pokemons de {}: ".format(self.nome))
            for pokemon in self.pokemons:
                print(pokemon)
                print("Status de {}".format(pokemon))
                print("hp---{}/{}\tlevel---{}\nExperiencia---{}/{}\tAtaque---{}\nEspecie---{}".format(pokemon.hp,(pokemon.lvl+20),pokemon.lvl,pokemon.experiencia,(2*pokemon.lvl + 300),pokemon.ataque,pokemon.especie))
            if a == True:
                curar = input(print("Deseja curar/reviver algum pokemon?(s/n)"))
                if curar == 's':
                    print("Insira o nome do pokemon a ser curado")
                    nome_poke = input()
                    for pokemon in self.pokemons:
                        if nome_poke == pokemon:
                            print("Escolha o item a ser usado")
                            self.mostrar_itens()
                            escolher_item = int(input())
                            for i in range(len(self.itens)):
                                if escolher_item == i:
                                    item_escolhido = self.itens[i]
                                    break
                            item_escolhido.action(pokemon)

                elif curar == 'n':
                    print("Seus pokemons te amam!")

        else:
            print("{} nao possui nenhum pokemon".format(self.nome))




    def escolher_aleatorio_pokemon(self):

        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}".format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("ERRO: O inimigo não possui pokemons disponives")


    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print("Voce ganhou ${}".format(quantidade))
        self.mostrar_dinheiro()


    def mostrar_dinheiro(self):
        print("Voce possui: ${} em sua conta".format(self.dinheiro))


class Player(Pessoa): #classe filha player
    tipo = "Players"


    def __str__(self): #Método para escolher o que será mostrado quando printar o objeto criado
        return self.nome


    def capturar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturado com sucesso!".format(pokemon))


    def mostrar_itens(self):
        for i in range(len(self.itens)):
            print("{} -- {} ".format(i,self.itens[i]))


    def adquirir_item(self):
        print("Escolha o item a ser comprado: ")
        print("1 -- Potion")
        print("2 -- Revive")
        escolha = int(input())

        while True:
            if escolha == 1:
                item = Potion(preco = 50)
                self.itens.append(item)
                self.dinheiro -= item.preco
                print("{} adquirido!".format(item))
                break
            elif escolha == 2:
                item = Revive(preco = 100)
                self.itens.append(item)
                self.dinheiro -= item.preco
                print("{} adquirido!".format(item))
                break
            else:
                print("Faça uma escolha valida")



    def escolher_pokemon(self):
        #print("Escolha um dos seus pokemons: ")
        i = 0
        for pokemon in self.pokemons:
            print("{} : {}".format(i,pokemon))
            i+=1
        while True:
            try:
                escolha = int(input("Eu escolho o pokemon de indice: "))
                return self.pokemons[escolha]
            except Exception as error:
                print("Escolha uma opção valida")
                print(error)


    def batalhar(self,pessoa):
        print("{} iniciou uma batalha com {}".format(self,pessoa))

        pessoa.mostrar_pokemons(False)
        pokemon_inimigo = pessoa.escolher_aleatorio_pokemon()

        meu_pokemon = self.escolher_pokemon()

        if meu_pokemon and pokemon_inimigo:
            while True:

                print("Escolha uma açao:")
                print("1 - atacar")
                print("2 - fugir")
                print("3 - usar item")
                acao = int(input())
                try:
                    if acao == 1:
                        vitoria = meu_pokemon.atacar(pokemon_inimigo,True)
                        if vitoria == True:
                            print("{} ganhou a batalha".format(self))
                            ganhei_dinheiro = pokemon_inimigo.lvl*100
                            self.ganhar_dinheiro(ganhei_dinheiro)
                            ganhei_exp = pokemon_inimigo.lvl +50
                            meu_pokemon.experiencia += (ganhei_exp)
                            meu_pokemon.passar_lvl()
                            break

                        vitoria_inimiga = pokemon_inimigo.atacar(meu_pokemon,False)
                        if vitoria_inimiga == True:
                            print("{} ganhou a batalha".format(pessoa))
                            break
                    if acao == 2:
                        chance_de_escapar = random.random()
                        if chance_de_escapar >=0.8:
                            print("voce conseguiu fugir da batalha")
                            break
                        else:
                            print("Voce nao conseguiu escapar da batalha e ainda vai tomar uma surra, volte a luta guerreiro!!")
                            vitoria_inimiga = pokemon_inimigo.atacar(meu_pokemon,False)
                            if vitoria_inimiga == True:
                                print("{} ganhou a batalha".format(pessoa))
                                break
                    if acao == 3:
                        print("Escolha o item a ser usado")
                        self.mostrar_itens()
                        escolher_item = int(input())
                        for i in range(len(self.itens)):
                            if escolher_item == i:
                                item_escolhido = self.itens[i]
                                break
                        item_escolhido.action(meu_pokemon)
                except ValueError:
                    print("Insira um valor dentro do range de opçoes valido")


        else:
            print("Nao eh possivel essa batalha ocorrrer")



    def explorar(self):
        a = random.random()
        if a <= 0.3:
            pokemon = random.choice(POKEMONS)
            print("Um pokemon selvagem apareceu!: {}".format(pokemon))
            escolha = input("Deseja capturar o pokemon? (s/n): ")
            while True:
                try:
                    if escolha == 's':
                        if random.random() >= 0.5:
                            self.capturar_pokemon(pokemon)
                            break
                        else:
                            print("O pokemon fugiu")
                            break
                    if escolha == 'n':
                        print("Voce deixou o pokemon ir embora")
                except:
                    print("Faça uma escolha valida")

        if a >= 0.7:
            inimigo = Inimigo()
            print("Um inimigo apareceu!")
            self.batalhar(inimigo)
        else:
            print("Essa exploração nao deu em nada")


class Inimigo(Pessoa): #Classe filha inimigo
    tipo = "Inimigo"


    def __init__(self, nome=None, pokemons=None):

        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)):
                pokemons_aleatorios.append(random.choice(POKEMONS))
            super().__init__(nome=nome, pokemons=pokemons_aleatorios) #Passa os pokemons aleatorios para o init da classe pai
        else:
            super().__init__( nome = nome, pokemons = pokemons )  # como já passei os pokemons, n faz nada


    def __str__(self):
        return self.nome


