def profit( t , c , M):
    #for table
    if t<= M :
        profit1= t*90
    else :
        profit1 = M*90 + (t-M)*100
    #for chair
    if c<=M :
        profit2 = c* 25
    else :
        profit2= M*25 + (c-M)*30
    return (profit1+profit2)

#Condition1
def constraint1(t,c):
    if (8*t + 2*c ) <=400:
        return True
    else :
        return False
    

#Condition2
def constraint2(t,c):
    if (2*t + c) <=120:
        return True
    else :
        return False

#Maximise_profit
def max_prof(M):
    max_p=0
    max_t=0
    max_c=0
    t1=[i for i in range(0,400//8)]
    c1=[i for i in range(0,(120//2))]
    for i in t1:
        for j in c1:
            if (constraint1(i,j) and constraint2(i,j))==True:
                prof = profit(i ,j , M)
                if prof>max_p:
                    max_p=prof
                    prof=profit(i,j,M)
                    max_t,max_c=i,j
                
    #returning maximum profit correspondingly the required no of tables and no of chairs
    return(max_p , max_t , max_c)

print( " M signifies the value after which profit value changes for each table and chair")
M=int(input("enter the value value Of M : "))
profit , table , chair= max_prof(M)

print ("maximum profit is  " ,profit, "for : ",table,"tables and  ",chair,"chairs ")
    
        
    
    
