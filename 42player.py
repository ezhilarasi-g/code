#ezhil
n=int(input())
lis=list(map(int,input().split()))
s=sorted(lis)
if s==lis:
    print("yes")
else:
    print("no")
