
def prop():

    tam = input("¿De que tamaño desea que sea la matriz?\n")
    tam = int(tam)
    print("Ingresa los datos iniciales")
    i = []
    i = [input("X" + str(j) + ": ") for j in range(tam)] 

    print("Ingresa los pesos iniciales")
    w = []
    w = [input("W" + str(j) + ": ") for j in range(tam)]
    
    
    b = 1
    for n in range(tam):
          for u in range(tam):
            res= int(i[n][u])*int(w[n][u]) + b
            return res

    
   

