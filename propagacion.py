
def prop():
    i = [[0.1,0.2],
         [0.2,0.4],
         [0.1,0.5],
         [0.2,0.3]]

    w = [[1.2,0.3],
         [1.1,0.5],
         [1.0,0.7],
         [0.7,0.5]]
    
    b = 1
    for n in range(3):
        for u in range(1):
            res= i[n][u]*w[n][u] + b
            return res

    
   

