 

entrada = open("tRalston.in","r")
saida = open("tRalston.out", "w" )

def dydx(x, y) :
 
    return eval(expressao)
 

def ralston(x0, y0, x, h) :
 
    #Encontrar o numero de iterações a partir de x,y e h:
    n = round((x - x0) / h)
    
    y = y0
     
    for i in range(1, n + 1) :
                
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)
 
        # ajusta y
        y = y + (1.0 / 6.0) * (k1 + 2 * k2)
 
        # ajusta x
        x0 = x0 + h
 
    return y
 
#main
  
for i, linha in enumerate(entrada):
    
    linha = linha.replace("\n","").split(";")

    expressao = linha[0]
    x0 = float(linha[1])
    y = float(linha[2])
    x = float(linha[3])
    h = float(linha[4])

    saidaStr = "y(x) = " + str(ralston(x0, y, x, h))

    print(saidaStr)
    saida.write(saidaStr)

entrada.close()
saida.close()
 
