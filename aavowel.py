#ezhil
n=input()
c=0
lis=['A','E','I','O','U','a','e','i','o','u']
for i in n:
    if i in lis:
        c=c+1
        break
if c!=0:
    print("yes")
else:
    print("no")
