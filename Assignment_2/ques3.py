#yearbook={"rohan":{"medha":1,"suresh":1,"suhana":1,"vishesh":1},"medha":{"rohan":0,"suresh":0,"suhana":1,"vishesh":0},"suresh":{"medha":1,"rohan":1,"suhana":0,"vishesh":0},"suhana":{"rohan":1,"suresh":1,"vishesh":0,"medha":1},"vishesh":{"rohan":1,"suresh":1,"suhana":1,"medha":1}}
'''file=open('file.txt','a+')
for i in yearbook:
    file.write(str(i)+str(yearbook[i]))'''

with open("file.txt", "r") as f:
    yearbook = {}
    for i in f:
        i = i.strip()
        #checks for emty string
        if i:
            if i.endswith(':'):
                c = i.strip(':')
                yearbook[c] = {}
            else:
                key, value = i.split(':')
                yearbook[c][key] = int(value)
count=0
#print(yearbook)
d2={}
for i in yearbook :
    d={}
    #data1=file.readline()
    #print(data1)
    count=0
    for j in yearbook[i] :
        count+=yearbook[i][j]
    d2[i]=count
#print(d2)
l,l1=[],[]
for i in d2 :
    if d2[i]==max(d2.values()):
        l+=[i]
    if d2[i]==min(d2.values()):
        l1+=[i]
print("most signatures :",[i for i in l],"no of signatures:",max(d2.values()))
print("least signatures :",[i for i in l1],"no of signatures:",min(d2.values()))
          
