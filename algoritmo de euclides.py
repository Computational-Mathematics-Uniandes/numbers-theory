

def algoritmo_euclides(x:int,y:int)->int:
    a=max(x,y)
    b=min(x,y)
    #El proceso iterativo es encontrar un entero e y un natural r, tal que 0=<r<e
    #Estos enteros deben satisfacer que a=b*e+r
    r=a%b#residuo
    print(str(a)+str('=')+str(b)+str('*')+str(a//b)+str('+')+str(r))
    if r!=0:
        #Si el residuo no es cero se continua el proceso iterativo
        return algoritmo_euclides(b,r)
    else:
        #cuando el residuo es cero se retorna b, que sería el MCD de (x,y)
        return b

        
        
        