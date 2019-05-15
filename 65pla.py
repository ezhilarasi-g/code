#ezhil
n=int(input())
a=list(map(int,input().split()))
d=[]
for i in a:
    if i<n:
        d.append(i)
        c=sorted(d)
print(*c)
