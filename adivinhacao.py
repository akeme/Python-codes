'''
   01 Algoritmo Jogo de Adivinhação 
    02 Variaveis:
    03     secreto, palpite: Inteiro
    04 Inicio
    05     SAIDA(“Bem-vindo ao jogo de adivinhação”)
    06     secreto = NUMERO_ALEATORIO(1,10)
    07 	 palpite = -1
    08     SAIDA(“Seu objetivo é acertar o número secreto”)
    09	 ENQUANTO palpite != secreto FACA
    10     	SAIDA(“Faça um palpite entre 1 e 10”)
    11		<Capture a entrada do jogador e coloque na variável palpite>
    12		SE palpite > secreto ENTAO
    13			SAIDA(“O número secreto é menor!”)
    14		FIM_SE
    15		SE palpite < secreto ENTAO
    16			SAIDA(“O número secreto é maior!”)
    17		FIM_SE
    18	 FIM_ENQUANTO
    19	 SAIDA(“Parabéns, você acertou!”)
    20 Fim

'''

import random

secreto  = random.randint(0, 10)
palpite = -1
print("Bem-vindo ao jogo de adivinhação")
while (palpite != secreto):
    print("Faça um palpite entre 1 e 10 ")
    palpite = int(input())
    if palpite > secreto:
        print("o número secreto é menor")
    if palpite < secreto:
        print("o número secreto é maior")
    else:
        print("parabéns você acertou")
