import math

#metodo da Bissecção

entrada = open("tSecante.in", "r")
saida = open("tSecante.out", "w")

#preparando as variaveis do arquivo.
#Elas são lidas na ordem: 
#   - Expressão f(x)
#   - a
#   - b
#   - parada (numero de interações)

expressao = "fx = " + entrada.readline()
a = float(entrada.readline())
b = float(entrada.readline())
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
    exit()

else:
    print("Existem Raízes. Calculando...")

    saida.write("n \t xn \t\t f(xn)\n")
    saida.write("0.\t %.6f \t %.6f\n" % (a,testeA))
    saida.write("1.\t %.6f \t %.6f\n" % (b,testeB))



# O programa fará a quantidade máxima de interações definida pelo usuário.
# Caso haja, o ponto de parada pro precisão terminará as interações antes
# da quantidade máxima.




for interacoes in range (2,parada):
    
# Para compreensão:
# c = x(k+1), a = x(k-1), b = x(k)

    x = a
    exec(expressao)
    fa = fx

    x = b
    exec(expressao)
    fb = fx

    c = b - ((fb)*(b-a)/(fb-fa))

    x = c
    exec(expressao)
    fc = fx

    saida.write("%d.\t %.6f \t %.6f\n" % (interacoes,c,fc))

    a = b
    b = c



        
#fim do Algoritmo

entrada.close()
saida.close()