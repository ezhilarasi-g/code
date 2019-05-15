#ezhil
a=int(input())
lis=list(map(int,input().split()))
lis1=[]
for i in lis:
    t=lis.count(i)
    lis1.append(t)
x=max(lis1)
print(x)
    
