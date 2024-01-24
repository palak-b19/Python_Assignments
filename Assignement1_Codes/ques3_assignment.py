x,y=0,0
x1,y1=x,y
d=1
distance=0
while d>0:
    d=int(input('enter distance : '))
    if d<=25 and d>=0:
        x,y=x,y+d
    elif d>=26 and d <=50:
        x,y=x,y-d
    elif d >=51 and d<=75:
        x,y=x+d,y
    elif d>=76:
        x,y=x-d,y
    distance+=d
print('final coordinates : ',x,',',y)
print('total distance travelled : ',distance)
distance_between= ((x1-x)**2 + (y1-y)**2)**(1/2)
print('straight line distance between initial and final location : ',distance_between)

