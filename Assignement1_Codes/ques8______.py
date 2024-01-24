p=[50,1450,1400,1700,1500,600,1200]
r=[0.025,0.021,0.017,0.013,0.009,0.005,0.001]

def current_pop(p,r,year):
    l1,r1=p,r
    l2,r2=[],[]
    pop=0
    for i in range(year):
        for i,j in zip(l1,r1) :
            l2+= [ (i + i*j)]
        l1=l2
        l2=[]
        for i in r1:
            r2+=[i-0.001]
        r1=r2
        r2=[]
    for i in l1:
        pop+=i
    return(pop)


def max_pop(p,r):
    year=1
    prev=0
    pop1=current_pop(p,r,year)
    while pop1 >=prev:
        year+=1
        prev=pop1
        pop1=current_pop(p,r,year)
    print('max population reached :' , prev)
    print('years after which max population reached:', (year-1))
      
max_pop(p,r)
