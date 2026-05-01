import numpy as np

def B_NR(f,df,n,a,b,tol):  
    iteraciones=0
    if f(a)*f(b)>0:
        print("- NO hay solución para el intervalo seleccionado (Bolzano no se cumple). -")
        return None, None, None, None
    elif f(a)*f(b)<0:
        for iteraciones in np.arange(0,n+1,1):
            c = (a+b) / 2
            if f(a)*f(c)<0: b=c
            elif f(b)*f(c)<0: a=c     
            else: # este else pretende cortar directamente el bucle de la biseccion si le pega a la raiz
                print("- Se hayo la raiz en el el metodo de biseccion sin llegar a N-R. -")
                return c, a, b, iteraciones+1
        # ------------------------------------------------------------------------------------------------
        # Continuamos con el metodo de N-R
        x0= (a+b) / 2
        if df(x0) == 0:
            print("- La derivada es cero. Newton no puede continuar. -")
            return None, None, None, None
        
        err=100 # valor inicial (solo para que entre al while)
        while err>tol:
            xn=x0-(f(x0)/df(x0))
            err=abs(xn-x0)
            x0=xn
            iteraciones=iteraciones+1
        return xn, a, b, iteraciones+1  
    
    else:    
        print("- Alguno de los puntos elegidos como intervalos es o son la raiz de la funcion -")
        return None, None, None, None