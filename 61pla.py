#ezhil
a,b=map(int,input().split())
lis=list(map(int,input().split()))
c=0
for i in lis:
    for j in lis:
        if i+j==b:
            c=1
            break
if c==1:
    print("yes")
else:
    print("no")
            
