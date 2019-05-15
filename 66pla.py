#ezhil
n,k=map(int,input().split())
lis=list(map(int,input().split()))
t=[]
b=[]
for i in lis:
    s=lis.count(i)
    if s==k:
        t.append(i)
a=set(t)
b=sorted(a)
print(*b)
