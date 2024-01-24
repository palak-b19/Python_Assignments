angle=float(input("enter the angle : "))
rad_angle= (angle * (3.14/180))
b=int(input("enter the horizontal distance : "))
def fact_(x):
    fact=1
    if x==0:
        return 1
    else :
        for i in range(1,(int(x)+1)):
            fact*=i
    return fact
factorial=fact_(rad_angle)

def sin_(x):
    term=0
    s=1
    for i in range (1,100,2):
        result=((s)*((x)**i))/fact_(i)
        term+=result
        s*=(-1)
    return (round(term,2))

def cos_(x):
    term=0
    s=1
    for i in range (0,100,2):
        result= ((s)*(x**i))/fact_(i)
        term+=result
        s*=(-1)
        
    return (round(term,2))
l=(b/(cos_(rad_angle)))

print("length of line from person to top of pole :", (b/(cos_(rad_angle))) )
print("height of to the top of pole : " , (l*(sin_(rad_angle))))
        
        
