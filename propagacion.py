
def prop():

    tam = input("¿De que tamaño desea que sea la matriz?\n")
    tam = int(tam)
    print("Ingresa los datos iniciales")
    i = []
    i = [input("X" + str(j) + ": ") for j in range(tam)] 

    print("Ingresa los pesos iniciales")
    w = []
    w = [input("W" + str(j) + ": ") for j in range(tam)]
    
    
    b = input("Ingresa el BIAS\n b: ")
    
    for n in range(tam):
     if(i[n]== ""):
          if(w[n]== ''):
            res= float(i[n])*float(w[n]) + float(b)
          else:
               print("El tamaño de los arreglos no coincide")

          return res

    
   

