# Implementação do Método de Heun
# Como os métodos agora imprimem gráficos,
# os arquivos de entrada devem ter apenas 
# uma linha. Multiplas linhas se mostraram 
# ineficientes, e podiam causar lentidão e 
# travamentos. Por isso, a ideia foi abandonada.

# organizar saída                                                                               ;


import math
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-poster')
#%matplotlib inline

entrada = open("tHeun.in","r")
saida = open("tHeun.out", "w")

def y1(t,y):

    sol = eval(expressao)

    return sol

# Entrada: Espreção, xI, xF, h, t0, y0                                                          ;

linha = entrada.readline()

linha = linha.replace("\n","").split(";")

expressao = linha[0]
xI = float(linha[1])
xF = float(linha[2])
h = float(linha[3])
x0 = float(linha[4])
y0 = float(linha[5])


t = np.arange(xI, xF, h)
y = np.zeros(t.size)
y[0] = y0

for i in range(1, t.size):

    y_i = y[i-1] + h*y1(t[i-1],y[i-1])
    y[i] = y[i-1] + (h/2.0)*(y1(t[i-1],y[i-1]) + y1(t[i],y_i))
    
#Debug Purposes
print(y)
print(t)

plt.figure(figsize = (10, 6))
plt.plot(t,y,'ro-')#t,yasol(t),'b-')
#plt.legend()
plt.show()

entrada.close()
saida.close()