from math import log
def f(t):
    return ((2000 * (log(140000/(140000 -2100*t)))) - (9.8*t))
def distance(a,b):
    d=0
    t=a
    while t!=b:
        v1=f(t)
        t+=0.25
        v2=f(t)
        avg_v= (v2+v1)/2
        d = d + (avg_v * 0.25)
    print('distance : ',d)
x=float(input("enter start time : "))
y=float(input("enter end time : "))
distance(x,y)
    
