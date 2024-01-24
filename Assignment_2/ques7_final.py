#d={}

def read1():
    d = {}
    with open("address_book.txt", 'r') as I:
        for line in I:
            if line!='':
                j = line.strip().split(',')
                #print(j)
                d2 = {}
                for part in j:
                    key, value = part.split(':')
                    d2[key] = value
                    #print(part)
                d[d2['Name']] = []
                for key, value in d2.items():
                    if key != 'Name':
                        d[d2['Name']].extend([key, value])
    return d


d = read1()
print(d)


#dictionary_made
#print(d)
def insert_new_entry():
    d=read1()
    f=open("address_book.txt",'a+')
    name=input("enter name \n")
    address=input("enter address \n")
    phone=input("enter phone number \n")
    email=input("enter email ID \n")
    if name in d :
        l2=["Address",address,"phone",phone,"email",email]
        d[name]=[d[name],l2]
    else:
        d[name]=["Address",address,"phone",phone,"email",email]
    f.write("Name:"+name+','+"Address:"+address+','+"Phone:"+phone+','+"Email:"+email+'\n')
    #print(d)

#insert_new_entry()

def delete1(y):
    d=read1()
    #print(d)
    z=0
    for i in d:
        if i==name :
            del(d[i])
            z=1
            break
    if z==0:
        print("record not found")
    #print(d)
    f=open("address_book.txt",'w+')
    for i in d :
        f.write("Name:"+i+','+d[i][0]+':'+d[i][1]+','+d[i][2]+':'+d[i][3]+','+d[i][4]+':'+d[i][5]+'\n')
    f.close()

def partial_name(y):
    d=read1()
    for i in d:
        if (y.lower()) in i or y in i or y==i or y.lower()==i:
            x=[j for j in d[i]]
            print(i)
            for k in x :
                print(k)
    

def phone_number(phone1):
    d=read1()
    y=d.keys()
    key=0
    for i in d:
        if d[i][3]==phone1:
            key=i
            break
    s=''
    if key!=0:
        l3=[j for j in d[key]]
        print(i)
        for k in l3:
            print(k)
        
    #print(d)
    
def email(email):
    d=read1()
    key1=0
    #print(d)
    for i in d :
        key1=0
        if d[i][5]==email:
            key1=i
        if key1!=0:
            l3=[j for j in d[key1]]
            print(i)
            for k in l3:
                print(k)
    #print(d)


while True:
    print('-'*50)
    print("enter the digits according to your task choice")
    print("1:insert an entry,2:delete an entry,3:partial name search,4:search by phone or email,5:exit")
    menu=int(input("enter your choice of digit \n"))
    if menu==1:
        insert_new_entry()
    if menu==2:
        name=input("enter name for which you want the record to be deleted: \n")
        delete1(name)
    if menu==3:
        partial1=input("enter partial name for which you want entires \n")
        partial_name(partial1)
    if menu==4:
        input2=input("enter p or e for phone or email \n")
        if input2=='p':
            input4=input("enter phone number \n")
            phone_number(input4)
        elif input2=='e':
            input5=input("enter email \n")
            email(input5)
        else:
            print("enter valid input")
    if menu==5:
        print("PROGRAM ENDED")
        break
    elif menu!=1 and menu!=2 and menu!=3 and menu!=4 and menu!=5:
        print(" enter valid input")
