#ezhil
n=int(input())
lis=list(map(int,input().split()))
c=0
for i in range(0,len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i]<lis[j]:
            c+=1
print(c)
