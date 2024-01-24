f = open("IPmarks.txt", "r+")
l=[]
for i in f:
    data=i.strip().split(',')
    l.append(data)
wts = [(10, 20), (20, 20), (100, 30), (40, 20),(80,10)]
#print(l)
print("roll no","total marks" , "     grade")
sum1=0
total1=0
for i in l:
    total1=0
    for j in range(1,len(i)):
        total= int(i[j])*(wts[j-1][1]/100)
        #print(int(i[j]))
        #print(wts[j-1][1])
        total1+=total
        #l2=[i[1] for i in wts]
        normalised= (total1)/52 *100
    total_marks = normalised 
    #print(total_marks)
    #print("ok")
    if total_marks >= 80:
        grade = 'A'
    elif total_marks >= 70:
        grade = 'A-'
    elif total_marks >= 60:
        grade = 'B'
    elif total_marks >= 50:
        grade = 'B-'
    elif total_marks >= 40:
        grade = 'C'
    elif total_marks >= 35:
        grade = 'C-'
    elif total_marks >= 30:
        grade = 'D'
    else:
        grade = 'F'
    print(i[0],total_marks,grade)
