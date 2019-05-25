#ezhil
n=int(input())
a=list(map(int,input().split()))
l=sorted(a)
dif=l[n-1]-l[0]
print(dif)
