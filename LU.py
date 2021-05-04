# Método Fatoração LU
import math
import numpy as np

entrada = open("tLu.in","r")
saida = open("tLu.out","w")

# A função "Fatora LU" recebe a Matriz A e 
# devolve duas matrizes: L e U para serem computadas. 

def fatoraLU(A):  
    U = np.copy(A)  
    n = np.shape(U)[0]  
    L = np.eye(n)  
    for j in np.arange(n-1):  
        for i in np.arange(j+1,n):  
            L[i,j] = U[i,j]/U[j,j]  
            for k in np.arange(j+1,n):  
                U[i,k] = U[i,k] - L[i,j]*U[j,k]  
            U[i,j] = 0  
    return L, U 

# Montando a Matriz na memória

matriz = []

linha = entrada.readline().split(",")
n = len(linha)
maplin = map(float,linha)
matriz.append(list(maplin))


for i in range(1,n):
    linha = entrada.readline().split(",")
    maplin = map(float,linha)
    linha = list(maplin)
    if len(linha) != n:
        print ("A matriz não é quadrada, e não pode ser resolvida com este método.")
        exit()
       
    matriz.append(linha)

# Vetor independente
linha = entrada.readline().split(",")
maplin = map(float,linha)
vetor = list(maplin)
if len(vetor) != n:
    print("O Vetor independente é de grandeza diferente da Matriz associada.")
    exit()

# Montando as Matrizes L, U a partir da Função.
#print(str(fatoraLU(matriz)))
mL, mU = fatoraLU(matriz) 

print(str(mL))
print(str(mU))

# Solucionando L * y = b | b = vetor

y = [0] * (n)
x = [0] * (n)

n = n-1
# vetor 1,2,3

for i in range (0,n):    
    y[i] = vetor[i]    
    for j in range(0, i):        
        y[i] = y[i] - (y[j] * mL[i][j])
    
    y[i] = y[i]/mL[i][i]

# Solucionando a U * x =  y

for i in range (n, -1, -1):
    x[i] = y[i]
    for j in range(i+1, n+1):
        x[i] = x[i] - (x[j] * mU[i][j])
    x[i] = x[i]/mU[i][i]


print (str(y), str(x))
