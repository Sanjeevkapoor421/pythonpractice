l=[]
grade=[]
names=[]
for _ in range(int(input())):
    name=input()
    marks=float(input())
    l.append([name,marks])
    grade.append(marks)
grade=sorted(set(grade))
m=grade[1]
for val in l:
    if val[1] == m:
        names.append(val[0])
names.sort()     
for i in names:
    print(i)
    