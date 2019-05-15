#ezhil
a,b=map(str,input().split())
s=0
for i in a:
    if i in b:
        s=1
        break
if s==1:
    print("yes")
else:
    print("no")
