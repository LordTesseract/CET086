#Método de Gauss-Seidel

import math
import numpy as np  
from numpy import linalg

def gauss_seidel(A,b,x0,tol,N):  
    #preliminares  
    A = A.astype(’double’)  
    b = b.astype(’double’)  
    x0 = x0.astype(’double’)  
 
    n=np.shape(A)[0]  
    x = np.copy(x0)  
    it = 0  
    #iteracoes  
    while (it < N):  
        it = it+1  
        #iteracao de Jacobi  
        for i in np.arange(n):  
            x[i] = b[i]  
            for j in np.concatenate((np.arange(0,i),np.arange(i+1,n))):  
                x[i] -= A[i,j]*x[j]  
            x[i] /= A[i,i]  
            print(x[i],A[i,i])  
        #tolerancia  
        if (np.linalg.norm(x-x0,np.inf) < tol):  
            return x  
        #prepara nova iteracao  
        x0 = np.copy(x)  
    raise NameError(’num. max. de iteracoes excedido.’)


entrada = open("tSeidel.in","r")
saida = open("tSeidel.out","w")

# Montando a Matriz na memória

matriz = []

linha = entrada.readline().split(",")
linhaSize = len(linha)
maplin = map(float,linha)
matriz.append(list(maplin))


for i in range(1,linhaSize):
    linha = entrada.readline().split(",")
    maplin = map(float,linha)
    linha = list(maplin)
    if len(linha) != linhaSize:
        print ("A matriz não é quadrada, e não pode ser resolvida com este método.")
        exit()
       
    matriz.append(linha)

# Vetor independente
linha = entrada.readline().split(",")
maplin = map(float,linha)
vetor = list(maplin)
if len(vetor) != linhaSize:
    print("O Vetor independente é de grandeza diferente da Matriz associada.")
    exit()






