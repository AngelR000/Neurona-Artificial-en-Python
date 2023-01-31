import propagacion
import math
pro = propagacion.prop()
e = math.e
try:  
    def act():
     a=1/(1+(e**(-pro)))
     return a
    if(pro): 
     print("Propagacion (Perceptron): " + str(pro))
except:
    print("¡La cantidad de datos ingresados no coincide con el tamaño de los arreglos!\n") 

