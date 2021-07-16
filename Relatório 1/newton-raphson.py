import math

#metodo da Bissecção

entrada = open("tNewton.in", "r")
saida = open("tNewton.out", "w")

#preparando as variaveis do arquivo.
#Elas são lidas na ordem: 
#   - Expressão f(x)
#   - a
#   - b
#   - parada (numero de interações)

expressao = "fx = " + entrada.readline()
derivada = "dx = " + entrada.readline()
a = float(entrada.readline())
parada = (int(entrada.readline()))
precisao = (int(entrada.readline()))

#analise de Funções Trigonometricas

expressao = expressao.replace("sen(", "math.sin(")
expressao = expressao.replace("cos(", "math.cos(")
expressao = expressao.replace("tan(", "math.tan(")


# O programa fará a quantidade máxima de interações definida pelo usuário.
# Caso haja, o ponto de parada pro precisão terminará as interações antes
# da quantidade máxima.




for interacoes in range (0,parada):
    
    x = a
    exec(expressao)
    exec(derivada)

    c = a - (fx/dx)


    saida.write("%d.\t %.6f \t %.6f\n" % (interacoes, a, c))    

    a = c

    


        
#fim do Algoritmo

entrada.close()
saida.close()
