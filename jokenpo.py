#    JOKENPO DO MOURA   # 

# aaaaaaaaaaaa meu teclado nao tem acento nem cedilha !! 

from operator import mod
from random import randint

# variaveis e ARMAZENAMENTO DE DADOS (jogadas e score)
jogadaP1 = 0
jogadaP2 = 0
jogadaC1 = (randint(1,3))
jogadaC2 = (randint(1,3))

p1Score = 0
p2Score = 0
c1Score = 0
c2Score = 0
modoJogo = 0
continuar = ""
sair = False
reset = ""



                    # Primeiro criarei funcoes para cada menu ( com bastante viadagens em ascii art )
def menuInicio():
    print("""
    _______                                   #                                                               #
---'   ____)                                         Oi,seja bem vindo ao pedra papel tesoura no python !        
      (_____)                                 #                                                               #
      (_____)                               
      (____)                                
---.__(___)                                 
""")                                            
    print("""                                                     |----------------------------------------------|
     _______                                         |   Para jogar player x player digite 1        |
---'    ____)____                                    |                                              |
           ______)                                   |  Para jogar player x computador digite 2     |
          _______)                                   |                                              |
         _______)                                    | Para jogar computador x computador digite 3  |
---.__________)                                      |----------------------------------------------|
""")
    print("""
    _______                                          |----------------------------------------------|
---'   ____)____                                     | Pedra = 1      Papel = 2    Tesoura = 3      |
          ______)                                    |----------------------------------------------|
       __________)
      (____)
---.__(___)
""")
    modoJogo = int(input("E ai, qual o modo de jogo? : "))
    return modoJogo
       
def menuScore():
    print(f"""
    _______                                                     |-------------------------------|
---'   ____)                                                    |Jogador 1: {p1Score} pontos!           |
      (_____)                                                   |Jogador 2: {p2Score} pontos!           |
      (_____)                                                   |Computador 1: {c1Score} pontos!        |
      (____)                                                    |Computador 2: {c2Score} pontos!        |
---.__(___)                                                     |-------------------------------|
""")                                    
    print("""
     _______                                             Para escolher o modo de jogo novamente digite RESET !
---'    ____)____
           ______)                          
          _______)                             
         _______)
---.__________)
""")
    print("""
    _______                                   #                                                                       #
---'   ____)____                                                       Obrigado por jogar !                          
          ______)                               Feito por: Eduardo Moura para a disciplina de Raciocinio Algoritmico
       __________)                                              ig/tt/git: @alwaystiredbtw
      (____)
---.__(___)                                   #                                                                       #
""")



#    FECHAR O LOOP GERAL PRA REINICIAR O JOGO  #
    reset = input(":")
    if reset == "reset":
        return False


                    # a escolha do modo de jogo esta na funcao do menu de apresentacao, recebendo um input e retornando o numero para a varialvel modojogo


                    # loop geral de funcionamento, desde a escolha do modo de jogo ate o placar final
while True:
                    # a escolha do modo de jogo esta na funcao do menu inicio, recebendo um input e retornando o numero para a varialvel modojogo
    modoJogo = menuInicio()


                    # criacao de funcao para cada modo de jogo( achei mais organizado assim so pra fechar certinho inves de ficar repetindo cada situacao )
    def pvp():
            print("O jogador I deve escolher sua jogada!")
            jogadaP1 = int(input("Jogada:"))
            print("O jogador II deve escolher sua jogada!")
            jogadaP2 = int(input("Jogada:")) 
            global p2Score
            global p1Score
            if jogadaP1 == 1:
                if jogadaP2 == 3:
                    print("Jogador I venceu a rodada!")
                    p1Score += 1
                elif jogadaP2 == 2:
                    print("Jogador II venceu a rodada!")
                    p2Score +=1
                else:
                    print("Empate")
            if jogadaP1 == 2:
                if jogadaP2 == 1:
                    print("Jogador I venceu a rodada!")
                    p1Score += 1
                elif jogadaP2 == 3:
                    print("Jogador II venceu a rodada!")
                    p2Score +=1
                else:
                    print("Empate")           
            if jogadaP1 == 3:
                if jogadaP2 == 2:
                    print("Jogador I venceu a rodada!")
                elif jogadaP2 == 1:
                    print("Jogador II venceu a rodada!")
                    p2Score +=1
                else:
                    print("Empate")
    def pvc():
            print("O jogador I deve escolher sua jogada!")
            jogadaP1 = (input("Jogada:"))
            print(f"O computador jogou {jogadaC1} ")
            global p1Score
            global c1Score
            global c2Score
            if jogadaP1 == 1:
                if jogadaC1 == 3:
                    print("Jogador I venceu a rodada!")
                    p1Score += 1
                elif jogadaC1 == 2:
                    print("Computador venceu a rodada!")
                    c1Score +=1
                else:
                    print("Empate")
            if jogadaP1 == 2:
                if jogadaC1 == 1:
                    print("Jogador I venceu a rodada!")
                    p1Score += 1
                elif jogadaC1 == 3:
                    print("Computador venceu a rodada!")
                    c1Score +=1
                else:
                    print("Empate")           
            if jogadaP1 == 3:
                if jogadaC1 == 2:
                    print("Jogador I venceu a rodada!")
                    p1Score += 1
                elif jogadaC1 == 1:
                    print("Computador venceu a rodada!")
                    c1Score +=1
                else:
                    print("Empate")
    def cvc():
            global c1Score
            global c2Score
            print(f"O computador I jogou {jogadaC1}")
            print(f"O computador II jogou {jogadaC2}")
            if jogadaC1 == 1:
                if jogadaC2 == 3:
                    print("Computador I venceu a rodada!")
                    c1Score += 1
                elif jogadaC1 == 2:
                    print("Computador II venceu a rodada!")
                    c2Score +=1
                else:
                    print("Empate")
            if jogadaC1 == 2:
                if jogadaC2 == 1:
                    print("Computador I venceu a rodada!")
                    c1Score += 1
                elif jogadaC1 == 3:
                    print("Computador I venceu a rodada!")
                    c2Score +=1
                else:
                    print("Empate")           
            if jogadaC1 == 3:
                if jogadaC2 == 2:
                    print("Computador I venceu a rodada!")
                    c1Score += 1
                elif jogadaC1 == 1:
                    print("Computador II venceu a rodada!")
                    c2Score +=1
                else:
                    print("Empate") 
    # apos escolher o modo de jogo, criarei cada situacao utilizando um loop infinito com while que +
    # sera quebrado apenas quando o jogador digitar o comando SAIR utilizando o False
    # rodando o jogo, quebrando ou continuando o loop \/
    while sair == False:
        jogador1Nome = "Jogador I"
        jogador2Nome = ""
        match modoJogo:
            case 1:
                pvp()
                jogador2Nome = "Jogador II"
                score1 = p1Score
                score2 = p2Score
            case 2:
                pvc()
                jogador2Nome = "Computador I"
                score1 = p1Score
                score2 = c1Score
            case 3:
                cvc()
                jogador1Nome = "Computador I"
                jogador2Nome = "Computador II"
                score1 = c1Score
                score2 = c2Score
        print(f"""                |-----------------------------------------------|
                |   {jogador1Nome}: ({score1})/{jogador2Nome} ({score2})               |
                | Para jogar novamente digite CONTINUAR         |
                | Para sair digite SAIR                         |
                |                                               |
                |-----------------------------------------------|""")

        continuar = input(":").upper()
        if continuar == "CONTINUAR":
            continue
        else: 
            break
    menuScore()
    
    
    
    




# Receita bolo de cenoura
# Bata os ovos com a cenoura, o açúcar, o leite (ou suco de laranja) e o óleo no liquidificador por cerca de 4 minutos ou até obter uma mistura uniforme.
#Despeje sobre a farinha misturada com o fermento e mexa até incorporar completamente.
#Disponha em fôrma retangular (22 x 32 cm) untada e enfarinhada.
#Asse em forno médio preaquecido (200 ºC) por cerca de 40 minutos ou até dourar.
#Depois de morno, regue com a calda de chocolate, polvilhe granulado e sirva em pedaços.
#Cobertura
#Dilua o amido no leite em uma panela.
#Junte o açúcar e o chocolate em pó e leve ao fogo médio, mexendo sempre, até encorpar.
#Variação
#Se preferir, substitua a cobertura por 150 g de raspas de chocolate ao leite ou meio amargo. Distribua sobre o bolo quente e espalhe com as costas de uma colher.
