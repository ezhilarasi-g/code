#ezhil
n=int(input())
l=list(map(int,input().split()))
f=0
for i in range(0,len(l)-1):
    f=f+max(l[i],l[i+1])
print(f)
