#    JOKENPO DO MOURA   # 
 

from random import randint

# variaveis e ARMAZENAMENTO DE DADOS (jogadas e score)
jogadaP1 = 0
jogadaP2 = 0
jogadaC1 = 0
jogadaC2 = 0

p1Score = 0
p2Score = 0
c1Score = 0
c2Score = 0
modoJogo = 0
continuar = ""
sair = False
reset = ""

pedra = "Pedra 🤛"
papel = "Papel ✋"
tesoura = "Tesoura ✌"

emoji = ""
emoji2 = ""





                    # Primeiro criarei funcoes para cada menu 
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
---'   ____)____                                     | Pedra = 1 🤛  Papel = 2 ✋ Tesoura = 3  ✌    |
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
---'   ____)                                                    |Jogador I: {p1Score} pontos!           |
      (_____)                                                   |Jogador II: {p2Score} pontos!          |
      (_____)                                                   |Computador I: {c1Score} pontos!        |
      (____)                                                    |Computador II: {c2Score} pontos!       |
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
          ______)                               Feito por: Eduardo Moura, Andre Akim, Vittorio, Gilamr Denck
       __________)                                    para a disciplina de Raciocinio Algoritmico           
      (____)
---.__(___)                                   #                                                                       #
""")



#    FECHAR O LOOP GERAL PRA REINICIAR O JOGO  #
    reset = input(":").lower().strip()
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
            while jogadaP1 != 1 and jogadaP1 != 2 and jogadaP1 != 3:
                print ("Jogada invalida! Digite novamente")
                jogadaP1 = int(input("Jogada:"))
            print("O jogador II deve escolher sua jogada!")
            jogadaP2 = int(input("Jogada:"))
            while jogadaP2 != 1 and jogadaP2 != 2 and jogadaP2 != 3:
                print ("Jogada invalida! Digite novamente")
                jogadaP2 = int(input("Jogada:"))

            if jogadaP1 == 1:
                emoji = pedra
            if jogadaP1 == 2:
                emoji = papel
            if jogadaP1 == 3:
                emoji = tesoura
            if jogadaP2 == 1:
                emoji2 = pedra
            if jogadaP2 == 2:
                emoji2 = papel
            if jogadaP2 == 3:
                emoji2 = tesoura
            print(f"O jogador I jogou {emoji} \nO jogador II jogou {emoji2}")

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
                    p1Score += 1
                elif jogadaP2 == 1:
                    print("Jogador II venceu a rodada!")
                    p2Score +=1
                else:
                    print("Empate")
    def pvc():
            print("O jogador I deve escolher sua jogada!")
            jogadaP1 = int(input("Jogada:"))
            while jogadaP1 != 1 and jogadaP1 != 2 and jogadaP1 != 3:
                print ("Jogada invalida! Digite novamente")
                jogadaP1 = int(input("Jogada:"))
            jogadaC1 = (randint(1,3))


            if jogadaP1 == 1:
                emoji = pedra
            if jogadaP1 == 2:
                emoji = papel
            if jogadaP1 == 3:
                emoji2 = tesoura
            if jogadaC1 == 1:
                emoji2 = pedra
            if jogadaC1 == 2:
                emoji2 = papel
            if jogadaC1 == 3:
                emoji2 = tesoura
            print(f"O jogador I jogou {emoji} e o computador jogou {emoji2}")
            
            global p1Score
            global c1Score
            
            
            if jogadaP1 == 1 and jogadaC1 == 3:
                    print("Jogador I venceu a rodada!")
                    p1Score +=1
                    return p1Score
            elif jogadaP1 == 1 and jogadaC1 == 2:
                    print("Computador I venceu a rodada!")
                    c1Score += 1
                    return c1Score
            elif jogadaP1 == jogadaC1:
                    print("Empate")
            elif jogadaP1 == 2 and jogadaC1 == 1:
                    print("Jogador I venceu a rodada!")
                    p1Score +=1
                    return p1Score
            elif jogadaP1 == 2 and jogadaC1 == 3:
                    print("Jogador I venceu a rodada!")
                    c1Score +=1
                    return c1Score
            elif jogadaP1 == jogadaC1:
                    print("Empate")           
            elif jogadaP1 == 3 and jogadaC1 == 2:
                    print("Jogador I venceu a rodada!")
                    p1Score +=1
                    return p1Score
            elif jogadaP1 == 3 and jogadaC1 == 1:
                    print("Computador I venceu a rodada!")
                    c1Score +=1
                    return c1Score
            elif jogadaP1 == jogadaC1:
                    print("Empate") 
    def cvc():
            global c1Score
            global c2Score
            jogadaC1 = (randint(1,3))
            jogadaC2 = (randint(1,3))

            if jogadaC1 == 1:
                emoji = pedra
            if jogadaC1 == 2:
                emoji = papel
            if jogadaC1 == 3:
                emoji = tesoura
            if jogadaC2 == 1:
                emoji2 = pedra
            if jogadaC2 == 2:
                emoji2 = papel
            if jogadaC2 == 3:
                emoji2 = tesoura

            print(f"O computador I jogou {emoji} e o computador II jogou {emoji2}")
            
            
            if jogadaC1 == 1 and jogadaC2 == 3:
                    print("Computador I venceu a rodada!")
                    c1Score += 1
                    return c1Score
            elif jogadaC1 == 1 and jogadaC2 == 2:
                    print("Computador II venceu a rodada!")
                    c2Score += 1
                    return c2Score
            elif jogadaC1 == 2 and jogadaC2 == 1:
                    print("Computador I venceu a rodada!")
                    c1Score += 1
                    return c1Score
            elif jogadaC1 == 2 and jogadaC2 == 3:
                    print("Computador II venceu a rodada!")
                    c2Score +=1
                    return c2Score           
            elif jogadaC1 == 3 and jogadaC2 == 2:
                    print("Computador I venceu a rodada!")
                    c1Score += 1
                    return c1Score
            elif jogadaC1 == 3 and jogadaC2 == 1:
                    print("Computador II venceu a rodada!")
                    c2Score +=1
                    return c2Score
            elif jogadaC1 == jogadaC2:
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
        print(f"""                |-------------------------------------------------------------------------|
                |   {jogador1Nome}: ({score1})/{jogador2Nome} ({score2})                  
                | Para jogar novamente pressione ENTER                                 
                | Para sair digite SAIR                                                   
                |                                                                         
                |-------------------------------------------------------------------------|""")

        continuar = str(input(":")).upper().strip()
        if continuar == "":
            continue
        else: 
            break
    menuScore()
    
    
    
    




