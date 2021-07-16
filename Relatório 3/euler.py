#Falta polir / ready


# Método de Euler para solução de ADO de 1º grau.
# Há duas formas de encontrar a resposta.
# Uma e dar o valor alvo de X, para saber 
# o valor de y' para aquela instância. A 
# outra forma é definir a quantidade de interações.
# Caso ambas as opções não sejam dadas, retorna
# um erro.

# Padrão de entrada do arquivo:
# Definição de F(x,y), h, x0, y0, quantidade de iterações, f(xn);
# Para encontrar f(xn), quantidade de iterações deve ser 0;
# Para encontrar pela quantidade de iterações, f(xn) deve ser 0.


# function to be solved

entrada = open("tEuler.in", "r")
saida = open("tEuler.out", "w")

# método de Euler

for i, linha in enumerate(entrada):
        
    linha = linha.replace("\n","").split(";")

    expressao = "F = " + linha[0]
    h = float(linha[1])
    x0 = float(linha[2])
    y0 = float(linha[3])
    nTarget = int(linha[4])
    xn = float(linha[5])

    # Passo
    #if nTarget > 0 and h == 0:
    h = (xn-x0)/nTarget

    print('\n------------Solução-----------')
    print('------------------------------')    
    print('i\tx0\ty0\tslope\tyn')
    print('------------------------------')

    for j in range(nTarget):
        
        x = x0
        y = y0
        exec(expressao)
        slope = F

        yn = y0 + h * slope
        print("%d\t%.4f\t%.4f\t%0.4f\t%.4f"% (j,x0,y0,slope,yn) )
        print('------------------------------')
        y0 = yn
        x0 = x0+h
    
    print("\nAt x=%.4f, y=%.4f" %(xn,yn))
    print("\n\n* Slope is actually F(x,y) solved.")


entrada.close()
saida.close()
