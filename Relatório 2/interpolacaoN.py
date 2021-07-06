#Polinômios de Diferenças Divididas de Newton

from scipy.interpolate import make_interp_splinha
from sympy import lambdify, Symbol, parse_expr, simplify
import numpy as np
import matplotlib.pyplot as plt
import re

entrada = open("tInterpolacao.in", "r")
saida = open("tInterpolacao.out", "w")


for i, linha in enumerate(entrada):
    linha = re.sub('[\n]*','',linha)
    linha = linha.split(";")
    
    sequenciaPontos = []

    for i in linha:
        sequenciaPontos.append(np.array(i.replace('(', '').replace(')','').replace('\n', '').split(',')).astype(np.float))

    pontos = np.array(sequenciaPontos)

#divided values
    qtdPontos = len(pontos)
    coeficientes = np.zeros([qtdPontos, qtdPontos])

    coeficientes[:,0] = pontos[:,1]
    
    for j in range(1,qtdPontos):
        for i in range(qtdPontos-j):
            coeficientes[i][j] = \
           (coeficientes[i+1][j-1] - coeficientes[i][j-1]) / (pontos[i+j][0]-pontos[i][0])

    #newton
    polinomio = "{}".format(coeficientes[0][0])

    for i in range(1,qtdPontos):
        mainOperator = " + " if coeficientes[0][i] >= 0 else " - "
        polinomio = polinomio + " {} ({}".format(mainOperator, abs(coeficientes[0][i]))
        for j in range(0,i):
            mainOperator = " - " if pontos[j][0] >= 0 else " + "
            polinomio = polinomio + " * (x {} {})".format(mainOperator, abs(pontos[j][0]))
        polinomio = polinomio + ")"

    polinomioFormatado = str(simplify(polinomio))

    polinomio = lambdify(Symbol('x'), parse_expr(polinomioFormatado))

    arrayX = []
    arrayY = []
    valoresPrev = []

    for i in range(len(pontos)):
        arrayX.append(pontos[i][0])
        arrayY.append(pontos[i][1])
        valoresPrev.append(polinomio(pontos[i][0]))

    saida = open("result.txt", "a")
    saida.write("---------------Problem Nยบ {}-------------------\n".format(i+1))
    saida.write("Approximate equation found: Y = {}".format(polinomioFormatado))
    saida.write("\n\n")
    saida.close()

    if len(valoresPrev) > 3:
        nArrayX = np.linspace(min(arrayX), max(arrayX), 200)
        splinha = make_interp_splinha(arrayX, valoresPrev, k=3)
        smoothYValues = splinha(nArrayX)


        plt.scatter(arrayX, arrayY)
        plt.plot(nArrayX, smoothYValues, color='red')
        plt.show()
    else:
        plt.scatter(arrayX, arrayY)
        plt.plot(arrayX, valoresPrev, color='red')
        plt.show()


entrada.close()
saida.close()
