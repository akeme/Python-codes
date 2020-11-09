'''
Algoritmo AV5

Variáveis

   numero, p, i : Inteiro

Início

   p = 0

   i = 0

   numero = 5

   ENQUANTO numero > 0 FAÇA

       SE numero % 2 == 0 ENTÃO

           p++

       SENÃO

           I++

       FIM_SE

       numero--

   FIM_ENQUANTO

Fim

'''
n = 5
p = 0
i = 0

while n > 0:
    if (n%2 == 0):
        p +=1
    else:
        i += 1
    n -= 1

print(n,p,i)
