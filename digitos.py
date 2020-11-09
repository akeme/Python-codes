'''

Algoritmo AV3

Variáveis

   valor, digitos : Inteiro

Início

   SAÍDA(“Informe um valor inteiro positivo”)

   ENTRADA(valor)

   digitos = 0

   ENQUANTO valor > 0 FAÇA

       valor = valor / 10

       digitos++

   FIM_ENQUANTO

   SAÍDA(digitos)

Fim

 
'''

print ("Informe um valor inteiro positivo")
valor = int(input())
digitos = 0

while valor > 0:
    valor = valor//10 #divisão inteira
    digitos += 1
    print(digitos)

print("qtd de digitos", digitos)
