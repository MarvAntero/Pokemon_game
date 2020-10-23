from Pessoa import*
from Pokemon import *
from Item import *
import pickle # Transforma qualquer objeto do python em bytes


def menu():
    print("-----------------------------------------")
    print("Escolha uma das ações a ser realizada: ")
    print("1 -- Explorar o mundo")
    print("2 -- Mostrar pokemons")
    print("3 -- Mostrar dinheiro")
    print("4 -- Ir a loja adquirir item")
    print("5 -- Batalhar com Rival")
    print("6 -- Batalhar com inimigo aleatorio")
    print("7 -- Salvar Jogo")
    print("8 -- Sair do jogo")
    print("------------------------------------------")

def menu_inicial():
    print("Bem vindo ao game Pokemon RPG")
    print("Escolha uma das opcoes:")
    print("1 -- Novo Jogo")
    print("2 -- Carregar jogo\n")

def salvar_game(player,rival):
    try:
        with open("database.db","wb") as arquivo: # modo de escrita para escrever em um arquivo binario
            dados = [player,rival]
            pickle.dump(dados,arquivo)# função para pegar os bytes e jogar em um arquivo -- passa o player e o arquivo no qua deseja jogar os bytes
            print("Jogo salvo com sucesso")

    except Exception as error:
        print("O seguinte erro ocorreu ao tentarmos salvar o game:")
        print("ERRO: {}".format(error))
def load_game():
    try:
        with open("database.db",'rb') as arquivo: # Modo de leitura para ler um arquivo binario
            dados = pickle.load(arquivo) #transforma o arquivo de volta em um objeto do tipo player
            print("Jogo carregado com sucesso")
            return dados

    except Exception as error:
        print("O seguinte erro ocorreu ao tentarmos carregar o game:")
        print("ERRO: {}".format(error))


def escolher_pokemon_inicial(player):

    print("Olá {}, está na hora de escolher seu pokemon inicial.".format(player))

    bulbassauro = PokemonGrama("Bulbassauro", lvl = 1)
    charmander = PokemonFogo("Charmander", lvl = 1)
    squirtle = PokemonAgua("Squirtle", lvl = 1)

    print("Escolha um dos tres pokemons abaixo: ")
    print("1 - ",bulbassauro)
    print("2 - ",charmander)
    print("3 - ",squirtle)

    while True:
        try:
            escolha = int(input("Escolha o seu Pokemon: "))
            if escolha == 1:
                player.capturar_pokemon(bulbassauro)
                break
            elif escolha == 2:
                player.capturar_pokemon(charmander)
                break
            elif escolha == 3:
                player.capturar_pokemon(squirtle)
                break
            else:
                print("Escolha invalida")
        except ValueError:
            print("Faça uma das escolhas propostas no menu")

if __name__ == "__main__":
    print("------------------------------------------------------")
    menu_inicial()
    escolha1 = int(input())
    try:
        if escolha1 == 1:
            rival = Inimigo("Gary", pokemons=[PokemonAgua("Squirtle", lvl=1)])
            nome = input("Qual eh o seu nome: ")
            player = Player(nome, pokemons = [])
            print("------------------------------------------------------")

        #Historia
            print("Olá {}, esse é um mundo habitado por pokemons, a partir de agora sua missao eh se tornar um mestre pokemon".format(player))
            print("Capture o maximo de pokemons que conseguir e lute com seus inimigos")
            print("Voce não tem nenhum pokemon, portanto precisa escolher um, vá encontrar o professor Oak e faça sua escolha")
            escolher_pokemon_inicial(player)
            print("Boa sorte no inicio de sua jornada, saia da cidade e vá se aventurar!!")
            print("Saindo da porta da sua cidade, voce encontra uma pessoa maltratando um pokemon e decide pará-lo...")
            print("A pessoa se chama {} e te desafia para uma batalha!!!".format(rival))
            player.batalhar(rival)
            print("Apos a batalha, {} diz que ainda voces ainda vao se encontra novamente e vai embora proferindo palavras feias.\n Parece que voce conseguiu um rival".format(rival))
        elif escolha1 == 2:
            dados = load_game()
            player = dados[0]
            rival = dados[1]
    except:
        print("Ocorreu um erro")



    while True:
        menu()
        escolha = int(input())
        try:
            if escolha == 1:
                player.explorar()
            elif escolha == 2:
                player.mostrar_pokemons(True)
            elif escolha == 3:
                player.mostrar_dinheiro()
            elif escolha == 4:
                player.adquirir_item()
            elif escolha == 5:
                player.batalhar(rival)
            elif escolha == 6:
                inimigo_aleatorio = Inimigo()
                player.batalhar(inimigo_aleatorio)
            elif escolha == 7:
                salvar_game(player,rival)
            elif escolha == 8:
                print("Até breve!!!")
                break
            else:
                print("Insira uma escolha valida!!")

        except ValueError:
            print("Valor inserido errado")
