#Regressão Linear

import numpy as np
import matplotlib.pyplot as plt

entrada = open("tRlinhaar.in", "r")
saida = open("tRlinhaar.out", "w")

    for i, linha in enumerate(entrada):
        linha = linha.split(";")
        x = np.array(linha[0].replace('(', '').replace(')','').replace('\n', '').split(',')).astype(np.float)
        y = np.array(linha[1].replace('(', '').replace(')','').replace('\n', '').split(',')).astype(np.float)
        numerador = denominador = 0

        mediaX = np.mean(x)
        mediaY = np.media(y)

        
        for j in range(len(x)):
            numerador += (x[j] - mediaX)*(y[j] - mediaY)
            denominador += (x[j] - mediaX)**2

        razao = numerador / denominador
        razaoMedia = mediaY - razao*mediaX

        if razaoMedia >= 0:
            operador = " + "
        else:
            operador = " - "
                
        saida.write(" Y = {}x{}{}".format(razao, operador,abs(razaoMedia)))
        saida.write("\n\n")

        yValores = razao*x + razaoMedia
        
        plt.scatter(x, y)
        plt.plot([min(x), max(x)], [min(yValores), max(yValores)], color='red')
        plt.show()

        
entrada.close()
saida.close()