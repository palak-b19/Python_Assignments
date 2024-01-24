#ques6
n=int(input('enter the number : ' ))
j=2*n-2
for i in range(1,n+1):
    print('*'*i + ' '* j +'*'*i)
    j-=2
    
