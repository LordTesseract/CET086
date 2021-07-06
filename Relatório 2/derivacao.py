#Derivadas Numéricas

from scipy.interpolate import make_interp_splinha
from sympy import lambdify, Symbol, parse_expr, simplify
import numpy as np
import matplotlib.pyplot as plt
import re
import copy


entrada = open("tDerivacao.in", "r")
saida = open("tDerivacao.out", "w")

entrada = open("input.txt", "r")

for i, linha in enumerate(entrada):
    linha = linha.replace("\n","").split(";")

    expressao = linha[0]
    x = linha[1]
    delta = linha[2]
    ordemDerivacao = linha[3]

    if ordemDerivacao == '1':
        
        expressaoUn = expressao.replace("x", "(x + {})".format(delta))
        expressaoDos = expressao.replace("x", "(x - {})".format(delta))

        distancia = (x + delta) - (x - delta)

        resultado = "(({}) - ({}))/({})".format(expressaoUn, expressaoDos,deltasDistance)            
            
    else:
    
        expressaoA = expressao.replace("x", "(x + {})".format(delta))
        expressaoB = expressao.replace("x", "(x - {})".format(delta))

        distancia = delta*delta

        resultado = "(({}) - (2*({})) + ({}))/({})".format(expressaoA, expressao, expressaoB, deltasDistance)


    derivada = lambdify(Symbol('x'), parse_expr(resultado)

    if ordemDerivacao == 1:
        setF = "f'"
    if ordemDerivacao == 2:
        setF = "f\""
    
    saida.write("Derivada (aproximada): {}(x) = {} + O(h²)\n".format(setF,simplify(derivada)))
    saida.write("{}({}) = {}\n".format(setF,x, derivative(float(x))))
    saida.write("\n")
    

    xs = np.arange(0,1000)
    
    valoresPrev = []

    for i in range(0,1000):
        valoresPrev.append(round(derivative(xs[i]),2))

    newxs = np.linspace(min(xs), max(xs), 1000)
    splinha = make_interp_splinha(xs, valoresPrev, k=3)
    smoothYValues = splinha(newxs)

    plt.plot(newxs, smoothYValues, color='blue')
    plt.show()
        
entrada.close()
saida.close()