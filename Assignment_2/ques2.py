
course=0
sum1, count = 0, 0
grade={'A+':10,'A':10,'A-':9,'B':8,'B-':7,'C':6,'C':5,'D':4,'F':2}
l=[]
grade1,sum1,credits1,score=0,0,0,0
y1=0
while True:
    l1=[]
    x1=input("Course no \n")
    for i in range(len(x1)):
        if x1[i].isalpha():
            start=i
    for i in range(len(x1)):
        if (x1[start+1:]).isdigit():
            y1=1
    if x1=='':
        break
    elif x1[0].isalpha()!=True or x1[0:start+1].isupper()!=True or x1[-1].isdigit()!=True or y1==0:
        print("incorrect course no ")
        continue
    x2=input('enter number_of_credits : \n')
    if x2.isdigit()==False or ( x2 not in '124'):
        print("incorrect credit")
        continue
    x3=input('enter grade_received : \n')
    if x3 not in grade:
        print("incorrect grade")
        continue
    else:
        for i in grade:
            if i==x3 :
               grade1=grade[i]
               grade2=i
        #l1=[x1,grade1]
        l1=[x1,grade2]
        l.append(l1)
    if x1=='':
        break
    else:
        score+=(grade1*int(x2))
        credits1+=int(x2)
l.sort()
#print(l)
print('-'*20+'TRANSCRIPT'+'-'*20)
for i in l:
    print(i[0],':' ,i[1])
result=score/credits1
print('SGPA :', round(result,2))
print('-'*50)
