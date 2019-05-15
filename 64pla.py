#ezhil
n,k=map(int,input().split())
a=list(map(int,input().split()))
d=[]
for i in a:
    if i<k:
        d.append(i)
        c=sorted(d)
print(*c)
