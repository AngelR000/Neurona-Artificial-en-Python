import propagacion
import math
pro = propagacion.prop()
e = math.e
def act():
    a=1/(1+(e**(-pro)))
    return a