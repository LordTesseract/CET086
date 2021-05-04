# Método de Eliminação de Gauss

import math

entrada = open("tGauss.in","r")
saida = open("tGauss.out","w")

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


#Algoritmo para o método:

n = n


for k in range(0,n):
    maximo = abs(matriz[k][k])
    maxindex = k
    for i in range(k,n):
        if maximo < abs(matriz[i][k]):
            maximo = abs(matriz[i][k])
            maxindex = i
    if(maxindex != k):
        for i in range (0,n):
            temp = matriz[k][j]
            matriz[k][j] = matriz[maxindex][j]
            matriz[maxindex][j] = temp
        temp2 = vetor[k]
        vetor[k] = vetor[maxindex]
        vetor[maxindex] = temp2

    if matriz[k][k] == 0:
        print("o sistema é impossível ou não tem solução única: Determinante = 0.")
        exit()
    else:
        for m in range(k+1, n):
            F = (-1) * matriz[m][k]/matriz[k][k]
            matriz[m][k] = 0
            vetor[m] = vetor[m] + F * vetor[k]
            for l in range(k+1, n):
                matriz[m][l] = matriz[m][l] + F * matriz[k][l]

    
X = [0] * (n)

n = n-1

X[n] = (vetor[n]/matriz[n][n])

for i in range (n, -1, -1):
    X[i] = vetor[i]
    for j in range(i+1, n+1):
        X[i] = X[i] - (X[j] * matriz[i][j])
    X[i] = X[i]/matriz[i][i]

for i in range(0,n+1):
    saida.write(str(matriz[i]) + "\n")
saida.write("Vetor Independente: " + str(vetor) + "\n")
saida.write("Solução: " + str(X) + "\n")



entrada.close()
saida.close()



