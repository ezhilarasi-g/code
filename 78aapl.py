#ezhil
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=a+b
lis=sorted(l)
res=''
for i in lis:
    res=res+str(i)+' '
print(res.strip())
