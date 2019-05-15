#ezhil
n=int(input())
lis=list(map(int,input().split()))
lis1=sorted(lis)
s=lis1[::-1]
res=''
for i in range(len(s)):
    res=res+str(s[i])+''
print(res)
