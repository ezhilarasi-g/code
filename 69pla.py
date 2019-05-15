#ezhil
a,b=map(int,input().split())
lis=list(map(int,input().split()))
res=''
c=a-b
for i in range(c):
    res=res+str(lis[i])+' '
print(res.strip())
