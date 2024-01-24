li=[]
while True:
    s=input("do u want to enter corrdinate : enter y/n : \n")
    if s=='y':
        x=int(input("enter x corrdinate \n"))
        y=int(input("enter y coordinate \n"))
        t=(x,y,1)
        li.append(t)
    else:
        break
#scaling parameters
cx=int(input("enter scaling parameter 1 : \n"))
cy=int(input("enter scaling paramter 2 : \n"))
lo=[[cx,0,0],[0,cy,0],[0,0,1]]
#matrix multiplication
def matrix_mult(l1,l2):
    l11=[]
    for i in range(len(l1)):
        l21=[]
        for j in range(len(l2[0])):
            sum1=0
            for k in range(len(l1[0])):
                product=(l1[i][k])*(l2[k][j])
                sum1+=product
            l21.append(sum1)
        l11.append(l21)
    return l11

result1=matrix_mult(li,lo)
#result_printing
t1=()
for i in result1:
    t=()
    t+=(i[0],)
    t+=(i[1],)
    t1+=(t,)
coordinates=str(t1)
print("coordinates of scalad matrix are : \n ",coordinates )

