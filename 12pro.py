#ezhil
a,b=map(int,input().split())
lis=list(map(int,input().split()))
lis1=sorted(lis)
d=lis1[::-1]
print(d[b-1])
