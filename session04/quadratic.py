import math

def quadratic(a,b,c):
    
    from math import sqrt

    a = float(a)
    b = float(b)
    c = float(c)
    d= b**2 - 4*a*c  
  
    if d >= 0:
        x1 = (-b+sqrt((b**2)-(4*(a*c))))/(2*a)
        x2 = (-b-sqrt((b**2)-(4*(a*c))))/(2*a)
        print ("This equation has two solutions: ", x1, x2)

    else:
        print('This equation has no roots.')

quadratic(1,4,-9)