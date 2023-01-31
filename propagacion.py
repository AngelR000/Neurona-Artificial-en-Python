
def prop():

    tam = input("¿De que tamaño desea que sea la matriz?")
    tam = int(tam)
    i = []
    i = [input("Dame los datos iniciales") for j in range(tam)] 

    w = []
    w = [input("Dame los pesos iniciales") for j in range(tam)]
    
    
    if(len(i)< len(w)):
     print("El tamaño de las matrices no coincide")
    if(len(w)< len(i)):
     print("El tamaño de las matrices no coincide")
     
    
    b = 1
    for n in range(tam):
          for u in range(tam):
            res= int(i[n][u])*int(w[n][u]) + b
            return res

    
   

