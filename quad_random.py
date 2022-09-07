import math
import random

def quadratica(a,b,c):
    delta=b**2-4*a*c
    if(delta>=0):
        x1=(-b-math.sqrt(delta))/(2*a)
        x2=(-b+math.sqrt(delta))/(2*a)
        print( "x1= ",x1,"\nx2= ",x2)

for a in range (-10,10):
    for b in range (-10,10):
        for c in range (-10,10):
            if (b*c==0):
                quadratica(a,b,c)