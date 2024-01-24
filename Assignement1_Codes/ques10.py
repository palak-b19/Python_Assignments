def p(x):
    return (x**3 - 10.5*x**2 + 34.5*x - 35)
def diff_p(x):
    return (3*x**2 - 10.5*2*x + 34.5)
def root(x,y,m):
    term= ((x*m - y)/m)
    return term
x=float(input("enter value "))
b=False
for i in range(1,100):
    if (-0.2< p(x) <0.2):
        b=True
    else:
        x=root(x,p(x),diff_p(x))
        b=True
    
if b==False:
    print('Try a different value')

print("nearest root",x)
