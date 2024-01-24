#ques1
menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]
print('MENU')
print("Item-no","name","price")
count12=1
for i in menu:
    print(str(count12)+'.',i[0],':',i[1])
    count12+=1
print()
sum1, count = 0, 0
result=[]

while True:
    print("input format eg - 1 3 for 3 samosas")
    x=input("enter item number followed by quantity desired : \n")
    l=x.split()
    if x=='' or len(x)!=3:
        break
    else:
        index1=(int(l[0])-1)
        item, price = (menu[index1][0]),int(menu[index1][1])
        if item !=0:
            sum1 += int(l[1]) * price
            count += int(l[1])
            data=(item+' , '+l[1]+' , '+'Rs '+str(price*int(l[1])))
            result.append(data)
        else:
            print("Item not found in menu")
print('BILL')
print('-'*30)
for i in result:
    print(i)
print('-'*30)
print("TOTAL :", count, "items,", "Rs", sum1)


