#metodo da Bissecção

import math

entrada = open("tBisseccao.in", "r")
saida = open("tBisseccao.out", "w")

#preparando as variaveis do arquivo.
#Elas são lidas na ordem: 
#   - Expressão f(x)
#   - a
#   - b
#   - parada (numero de interações)

expressao = "fx = " + entrada.readline()
a = int(entrada.readline())
b = int(entrada.readline())
parada = (int(entrada.readline()))
precisao = (int(entrada.readline()))

precisao = 1 * (10 ** (-precisao))
print (precisao)

expressao = expressao.replace("sen(", "math.sin(")
expressao = expressao.replace("cos(", "math.cos(")
expressao = expressao.replace("tan(", "math.tan(")

#teste de raízes. Se o sinal inverte, há raízes. Senão, não há raízes.

x = a
exec(expressao)
testeA = fx

x = b
exec(expressao)
testeB = fx


if (testeA * testeB > 0):
    print ("Erro: Não existem raízes possíveis.")
    exit()

else:
    print("Existem Raízes. Calculando...")

    saida.write("Iter. \t an \t\t bn \t\t cn \t\t f(cn)\n")

#implementação do Algoritmo

for interacoes in range (1,parada):
    
    c = (a+b)/2

    x = c
    exec(expressao)
    fc = fx

    #txtSaida = str(interacoes) + str(a) + "\t\t\t" + str(b) + "\t\t\t" + str(c) + "\t\t\t" + str(fc) + "\n"
    #saida.write(txtSaida)
    saida.write("%d.\t %.4f \t %.4f \t %.4f \t %.4f\n" % (interacoes, a, b, c, fc))
    

    if (fc < 0):
        a = c
    else:
        b = c

        
#fim do Algoritmo

entrada.close()
saida.close()
