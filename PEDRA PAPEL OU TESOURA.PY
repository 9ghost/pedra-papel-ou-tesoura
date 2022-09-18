from random import choice


jogador_vitorias = 0 
maq_vitorias = 0

def Opcao_jogador():
    esc_jogador = input("Escolha Pedra, Papel ou Tesoura: ")
    esc_jogador.lower()
    if esc_jogador == "pedra":
        return esc_jogador
    elif esc_jogador == "papel":
        return esc_jogador
    elif esc_jogador == "tesoura":
        return esc_jogador
    else: 
        print ("Opção Inválida. Tente Novamente")
        Opcao_jogador()         

def Opcao_maquina():
    esc_maquina = choice(["pedra", "papel", "tesoura"])
    return esc_maquina



while True:
   
    print("-"*30)
    esc_jogador = Opcao_jogador()
    esc_maquina = Opcao_maquina()
    print("-"*30)
    
    if(esc_jogador == "pedra") and (esc_jogador == "tesoura") \
        or (esc_jogador == "papel") and (esc_maquina == "pedra")\
            or(esc_jogador == "tesoura") and (esc_maquina == "papel"):
            #Jogador ganha
            
            print(f"Jogador Escolheu {esc_jogador} e a Máquina escolheu {esc_maquina}"
            " Resultado: Você Ganhou!")
            jogador_vitorias += 1

    elif esc_jogador == esc_maquina:
        #Empate
        print(f"Jogador Escolheu {esc_jogador} e a Máquina escolheu {esc_maquina}"
            " Resultado: Empate!")
    else:
        #Maquina Ganha   
        print(f"Jogador Escolheu {esc_jogador} e a Máquina escolheu {esc_maquina}"
            " Resultado: Você Perdeu!")    
        maq_vitorias += 1             

    print("-"*30)
    print(f"vitorias do Jogador: {jogador_vitorias}")
    print(f"vitorias da maquina: {maq_vitorias}")
    print("-"*30)

    
    esc_jogador = input("Voce Quer Jogar Novamente? ")
    if esc_jogador in ["SIM","sim","Sim","S","s"]:
        pass
    elif esc_jogador in ["NAO","Nao","nao" ,"n","N"]:
        break
    else:
        break