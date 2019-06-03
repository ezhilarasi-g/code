#ezhil
n=input()
lis=[]
for i in n:
    if i!=' ':
        if i not in lis:
            low=i.lower()
            lis.append(low)
if len(lis)==26:
    print("yes")
else:
    print("no")
