n=int(input('enter a number n such that n>=0 and n< 1,00,00,000 : '))
p1=str(n)

d1={' ':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10}
d2={'twenty':2,'thirty':3,'forty':4,'fifty':5,'sixty':6,'seventy':7,'eighty':8,'ninety':9}
d3={'eleven':1,'twelve':2,'thirteen':3,'fourteen':4,'fifteen':5,'sixteen':6,'seventeen':7,'eighteen':8,'nineteen':9}
d4={'one hundred' :1,'two hundred':2,'three hundred':3,'four hundred':4,'five hundred':5,'six hundred':6,'seven hundred':7,'eight hundred':8,'nine hundred':9}
d5={'one' :1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}





def unit_digit(n):
    s1=''
    if n==0:
        print("zero")
    else :
        for i in d1:
            if d1[i]==n:
                s1+=i
    return (s1)
def ten_digit(n):
    s1=''
    y=n//10
    u1=n%10
    if (y==1 and u1!=0):
        for i in d3:
            if d3[i]==u1:
                s1+=i
    elif ( y==1 and u1==0):
        s1+='ten'
    else:
        t=n//10
        u=n%10
        for i in d2 :
            if d2[i]==t:
                s1+=i +' '
        if u==0:
            s1+=''
        else:
            s2=unit_digit(u)
            s1+=s2
    return(s1)

def hundred_digit(n):
    p=str(n)
    s1=''
    h=n//100
    digits=n%100
    t=n//10
    u1=t%10
    u2=n%10
    if (u1==0 and u2==0):
        for i in d4:
            if d4[i]==h:
                s1+=i
    elif (u1==0 and u2!=0):
        for i in d4:
            if d4[i]==h:
                s1+=i
        s2= unit_digit(u2)
        s1=s1 + ' and ' + s2
    else :
        for i in d4:
            if d4[i]==h:
                s1+=i
        s2= ten_digit(digits)
        s1= s1+ ' and ' + s2
    return (s1)

def thousand(n):
    p=str(n)
    s1=''
    thousanth=int(p[0])
    hundredth=int(p[1])
    tenth=int(p[2])
    unit=int(p[3])
    for i in d5:
            if d5[i]==thousanth:
                s1+=  i +' ' + 'thousand '
    if (hundredth==0 and tenth==0 and unit==0):
        s1+=''
    no=int(p[2:4])
    if ((hundredth==0 and tenth!=0 and unit!=0) or no==10):
        s2=ten_digit(no)
        s1= s1+ ' and ' + s2
    else :
        n2=int(p[1:4])
        s2= hundred_digit(n2)
        s1+=  s2
    return (s1)

def ten_thousand(n1):
    p2=str(n1)
    
    s1=''
    ten_thousanth,thousanth,hundredth,tenth,unit=int(p2[0]),int(p2[1]),int(p2[2]),int(p2[3]),int(p2[4])
    n0=int(p2[0:2])
    s2=ten_digit(n0)                                                       
    s1+=  s2 +' ' + 'thousand '
    n2=int(p2[2:6])
    s3=hundred_digit(n2)
    s1+=s3
    return s1

def lakh(n):
    p=str(n)
    s1=''
    lakh,ten_thousanth,thousanth,hundredth,tenth,unit=int(p[0]),int(p[1]),int(p[2]),int(p[3]),int(p[4]),int(p[5])
    n1=int(p[0])
    for i in d5 :
        if d5[i]==n1:
            s1+= i + ' lakh '
    if (ten_thousanth==0 and thousanth!=0 ):
        n2=int(p[2:6])
        s2=thousand(n2)
        s1+=' ' + s2
    elif(ten_thousanth==0 and thousanth==0 and hundredth!=0):
        n2=int(p[3:6])
        s2=hundred_digit(n2)
        s1+=' ' + s2
    elif (ten_thousanth==0 and thousanth==0 and hundredth==0 and tenth!=0):
        n2=int(p[4:6])
        s2=ten_digit(n2)
        s1+=' ' + s2
    elif (ten_thousanth==0 and thousanth==0 and hundredth==0 and tenth==0 and unit!=0):
        n2=int(p[5:6])
        s2=unit_digit(n2)
        s1+= ' '+ s2
    elif (ten_thousanth==0 and thousanth==0 and hundredth==0 and tenth==0 and unit==0):
        s1+=' '
    else :
        n2=int(p[1:6])
        
        s2= ten_thousand(n2)
        s1+=s2
    return s1

def ten_lakh(n1):
    p2=str(n1)
    
    s1=''
    ten_lakh,lakh,ten_thousanth,thousanth,hundredth,tenth,unit=int(p2[0]),int(p2[1]),int(p2[2]),int(p2[3]),int(p2[4]),int(p2[5]),int(p2[6])
    n0=int(p2[0:2])
    s2=ten_digit(n0)                                                       
    s1+=  s2 +' ' + ' lakh '
    if (ten_thousanth==0 and thousanth!=0 ):
        n2=int(p2[3:7])
        s2=thousand(n2)
        s1+=' ' + s2
    elif(ten_thousanth==0 and thousanth==0 and hundredth!=0):
        n2=int(p2[4:7])
        s2=hundred_digit(n2)
        s1+=' ' + s2
    elif (ten_thousanth==0 and thousanth==0 and hundredth==0 and tenth!=0):
        n2=int(p2[5:7])
        s2=ten_digit(n2)
        s1+=' ' + s2
    elif (ten_thousanth==0 and thousanth==0 and hundredth==0 and tenth==0 and unit!=0):
        n2=int(p2[6:7])
        s2=unit_digit(n2)
        s1+= ' '+ s2
    elif (ten_thousanth==0 and thousanth==0 and hundredth==0 and tenth==0 and unit==0):
        s1+=' '
    else :
        n0=int(p2[0:2])
        n2=int(p2[2:7])
        
        s2= ten_thousand(n2)
        s1+=s2
    return s1
    
    
if len(p1)==1:
    ans=unit_digit(n)
elif len(p1)==2:
    ans=ten_digit(n)
elif len(p1)==3:
    ans=hundred_digit(n)
elif len(p1)==4:
    ans=thousand(n)
elif len(p1)==5:
    ans=ten_thousand(n)
elif len(p1)==6:
    ans=lakh(n)
elif len(p1)==7:
    ans=ten_lakh(n)

print(ans)
    
