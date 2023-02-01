
def prop():
 try:
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
       res= float(i[n])*float(w[n]) + float(b)
    return res
 except:
          print("La cantidad de datos ingresados no coincide con el tamaño de los arreglos\n")

    
   

