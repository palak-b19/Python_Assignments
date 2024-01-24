cost=int(input('enter cost of the laptop : '))
def laptop_cost(allowance,sf,rate):
    savings=0
    month=1
    inst=1
    while ( savings<cost):
        savings+=sf*allowance
        inst=(savings*(0.5/100))
        if savings >= cost :
            break
        savings+=(inst)
        month+=1
    print('months after which laptop can be bought :',month)
    print('savings :' , (savings - cost) )
laptop_cost(20000,0.1,0.5)
    
    
