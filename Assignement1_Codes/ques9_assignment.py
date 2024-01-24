p=1.0
a,b,c,d= 10,1.05,1,1.0
demand,supply=0,0
from math import e
print(e**3)
flag=True
while flag==True:
    from math import e
    demand+=(e** ((10 -(1.05*p))))
    supply+=(e**((1 + (1.0*p))))
    p+=(0.05*p)
    if (abs(demand-supply))<2:
        print("eqbm price ",p,"eqbm demand ", demand, "eqbm supply :",supply)
        flag=False
        break
    
    
    
    
