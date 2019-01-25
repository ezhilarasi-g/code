#ezhil
a,b=map(int,input().split())
l=list(map(int,input().split()))
if b in l:
    print(l.count(b))
else:
    print("0")
