#ezhil
n=int(input())
lis=list(map(int,input().split()))
x=sorted(lis)
res=' '
for i in x:
	res=res+str(i)+' '
print(res.strip())
