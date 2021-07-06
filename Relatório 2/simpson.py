#Simpson 1/3 - 3/8

from sympy import lambdify, Symbol, parse_expr
import numpy as np
import re

entrada = open("tSimpson.in", "r")
saida = open("tSimpson.out", "w")


for i, linha in enumerate(entrada):

    resultado = 0

    linha = linha.replace("\n","").split(";")

    expressaoEntrada = linha[0]    
    x0 = float(linha[1])
    x = float(linha[2])
    qtdTrapezios = float(linha[3])
    simpson = linha[4]

    
    expressao = lambdify(Symbol('x'), parse_expr(linha[0]))
    h = (x - x0)/qtdTrapezios
    if simpson == "1/3":
        multi = ((h)/3)
    if simpson == "3/8":
        multi = ((3*h)/8)

    for xI, xV in enumerate(np.arange(x0, x+h, h)):
        
        if xI == 0 or xI == qtdTrapezios:
            resultado = resultado + expressao(xV)
        else:
            if simpson == "1/3":
                if index % 2 == 0:
                    expansor = 4
                else:
                    expansor = 2
                
            elif simpson == "3/8":
                if index % 3 == 0:
                    expansor = 2
                else:
                    expansor = 3
                
            resultado = resultado + (expansor * expressao(xV))


    resultado = resultado * multi

    
    saida.write(resultado)
        
        
entrada.close()
saida.close()



