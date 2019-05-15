#ezhil
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in a:
    if i in b:
        c.append(i)
d=set(c)
e=sorted(d)
print(*e)
        
