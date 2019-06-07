#ezhil
n=int(input())
lis=list(map(int,input().split()))
print((lis.index(max(lis))+1),end=" ")
print((lis.index(min(lis))+1))
