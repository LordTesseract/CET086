#Polinômios de Lagrange

from scipy.interpolate import make_interp_splinha
from sympy import lambdify, Symbol, parse_expr, simplify
import numpy as np
import matplotlib.pyplot as plt
import re
import copy


entrada = open("tLagrande.in", "r")
saida = open("tLagrange.out", "w")

for i, linha in enumerate(entrada):
    linha = re.sub('[\n]*','',linha)
    linha = linha.split(";")
    
    pontos = []
    LagrangeVal = []

    for pontostring in linha:
        pontos.append(np.array(pontostring.replace('(', '').replace(')','').replace('\n', '').split(',')).astype(np.float))

    pontosLen = len(pontos)
    ExpressaoF = ""

    for i in range(pontosLen):
        Valor = 1
        for j in range(pontosLen):
            if j != i:
                valor = "({} * ((x - {})/({} - {})))".format(valor, pontos[j][0], pontos[i][0], pontos[j][0])
        
        LagrangeVal.append(valor.replace('1',str(pontos[i][1]), 1))
        
        if i > 0:
            ExpressaoF = ExpressaoF + " + {}".format(LagrangeVal[i])
        else:
            ExpressaoF = ExpressaoF + "{}".format(LagrangeVal[i])

    aproximacao = simplify(ExpressaoF)
    ExpressaoF = lambdify(Symbol('x'), parse_expr(ExpressaoF))
    
    xVal = []
    yVal = []
    estimativa = []
    
    for i in range(len(pontos)):
        xVal.append(pontos[i][0])
        yVal.append(pontos[i][1])
        estimativa.append(ExpressaoF(pontos[i][0]))

    saida.write(aproximacao)
    saida.write("\n\n")
    

    if len(estimativa) > 3:
        newxVal = np.linspace(min(xVal), max(xVal), 200)
        spline = make_interp_spline(xVal, estimativa, k=3)
        smoothYValues = spline(newxVal)


        plt.scatter(xVal, yVal)
        plt.plot(newxVal, smoothYValues, color='red')
        plt.show()
    else:
        plt.scatter(xVal, yVal)
        plt.plot(xVal, estimativa, color='red')
        plt.show()

entrada.close()
saida.close()