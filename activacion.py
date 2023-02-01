import propagacion
import math
try:
 pro = float(propagacion.prop())
 e = math.e
  
 def act():
     a=1/(1+(e**(-1*pro)))
     return a
 if(pro): 
     print("Propagacion (Perceptron): " + str(pro))
except:
   print("¡No se logro ejecutar el calculo de activacion!\n") 

