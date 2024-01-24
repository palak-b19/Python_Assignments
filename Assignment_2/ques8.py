def read1():
    f =open("pages.txt",'r+')
    l=[]
    d={}
    list1=f.readlines()
    for i in list1:
        x=i.split(',')
        d[x[0]]=x[1]
    return d

d=read1()
#print(d)
d2={}
val=d.values()
for i in d:
    #print(i)
    for k in d[i].split():
        #print(k)
        if 'URL' in k :
            if i not in d2:
                d2[i]=[k]
            else:
                d2[i].append(k)
d_imp={}
for i in d:
    for j in d[i].split():
        #print(j)
        if '.' in j:
            d_imp[i]=float(j)
#print(d_imp)
#print(d2)
d_f={}
for i in d2:
    for j in d2[i]:
        #print(i,j)
        #print(d_imp[j])
        if j not in d_f:
            d_f[j]=(d_imp[i])/(len(d2[i]))
        else :
            d_f[j]+=(d_imp[i])/(len(d2[i]))
#print(d_f)        
x2=[(v, k) for k, v in d_f.items()]
x2.sort(reverse=True)
x3={k: v for v, k in x2}
#print(x3)
n=int(input("enter no of entries you want to be displayed : \n "))
print("highest ranking pages in descending order")
count=0
for i in x3:
    count+=1
    print("rank",count,i,' ','overall importance',x3[i])
    if count==n:
        break
    
