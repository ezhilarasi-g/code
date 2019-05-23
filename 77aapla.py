#ezhil
n=int(input())
l=list(map(int,input().split()))
c=1
lis=[]
for i in range(0,len(l)-1):
    if l[i]<l[i+1]:
        c=c+1
    else:
        lis.append(c)
        c=1
lis.append(c)
print(max(lis))
