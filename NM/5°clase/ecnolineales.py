import numpy as np

def Bisec(a,b,f,n):  
    if f(a)*f(b)>0:
        print("el intervalo no es valido")
        return
    elif f(a)*f(b)<0:
        for i in np.arange(0,n,1):
            c = (a+b) / 2
            if f(a)*f(c)<0: b=c
            elif f(b)*f(c)<0: a=c     
            else: 
                print("La raiz es",c)
                break 
        return c
    else:    
        print("Alguno de los puntos de los parametros es la raiz ")
        return
