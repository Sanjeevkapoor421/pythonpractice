print("enter the value : ")
n= int(input())
print("enter the string : ")
score=input()
out=[]
sec=[]
out=score.split(" ")
for i in range(0,n):
    out[i]=int(out[i])
out.sort(reverse=True)
m=max(out)
for i in range(0,n):
    if (out[i] != m):
        sec.append(out[i])
print(max(sec))