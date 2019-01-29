#ezhil
n,k=map(int,input().split())
lis=list(map(int,input().split()))
res=''
for i in range(k):
    temp=lis[-1]
    del(lis[-1])
    lis.insert(0,temp)
for i in range(len(lis)):
    res=res+str(lis[i])+' '
print(res.strip())
    
