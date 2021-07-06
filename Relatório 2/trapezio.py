#Integração por Trapézio

import numpy as np
import re
from sympy import lambdify, Symbol, parse_expr

entrada = open("tTrapezio.in", "r")
saida = open("tTrapezio.out", "w")

for i, linha in enumerate(entrada):

    resultado = 0

    linha = linha.replace("\n","").split(";")

    expressaoEntrada = linha[0]    
    x0 = float(linha[1])
    x = float(linha[2])
    qtdTrapezios = float(linha[3])
    
    expressao = lambdify(Symbol('x'), parse_expr(linha[0]))
    h = (x - x0)/qtdTrapezios

    for xI, xV in enumerate(np.arange(x0, x+h, h)):
        if xI == 0 or xI == qtdTrapezios+1:
            resultado = resultado + expressao(xV)
        else:
            resultado = resultado + (2 * expressao(xV))

    resultado = resultado * (h/2)

    
    saida.write(resultado)
        
        
entrada.close()
saida.close()
