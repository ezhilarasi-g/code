#ezhil
n,k=map(int,input().split())
a=list(map(int,input().split()))
c=sorted(a)
d=[]
for i in a:
    if i<k:
        d.append(i)
print(*d)
