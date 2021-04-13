import math

#metodo da Bissecção

entrada = open("entrada.in", "r")
saida = open("saida.out", "w")

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

#analise de Funções Trigonometricas

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

else:
    print("Existem Raízes. Calculando...")

    saida.write("n \t an \t\t\t bn \t\t\t cn \t\t\t f(cn)\n")

for interacoes in range (1,parada):
    
    c = (a+b)/2

    x = c
    exec(expressao)
    fc = fx    

    txtSaida = str(interacoes) + "\t" + str(a) + "\t\t\t" + str(b) + "\t\t\t" + str(c) + "\t\t\t" + str(fc) + "\n"

    saida.write(txtSaida)

    if (fc < 0):
        a = c
    else:
        b = c

        
#fim do Algoritmo

entrada.close()
saida.close()