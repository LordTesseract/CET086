#Falta Polir / Ready

# Implementação do método Runge-Kutta de 4ª ordem.

#Entrada: Espreção, x0, y, x, h

entrada = open("tKutta4.in","r")
saida = open("tKutta4.out","w")

def dydx(x, y):
    
    solucao = eval(expressao)
    return solucao
 
# Finds value of y for a given x using step size h
# and initial value y0 at x0.

def rungeKutta(x0, y0, x, h):   
    
    n = (int)((x - x0)/h)   
    y = y0

    for i in range(1, n + 1):
        # Apply Runge Kutta Formulas to find next value of y
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * dydx(x0 + h, y + k3)
 
        # Update next value of y
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
 
        # Update next value of x
        x0 = x0 + h
    return y
 
# Driver method
for i, linha in enumerate(entrada):
        
    linha = linha.replace("\n","").split(";")

    expressao = linha[0]
    x0 = float(linha[1])
    y = float(linha[2])
    x = float(linha[3])
    h = float(linha[4])

    print ("The value of y at x is: %0.6f" %(rungeKutta(x0, y, x, h)))

entrada.close()
saida.close()