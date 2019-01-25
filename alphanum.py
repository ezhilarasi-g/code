#ezhil
n=input()
c=0
for i in n:
    if i.isalpha():
        c=c+1
        break
for j in n:
    if j.isnumeric():
        c=c+1
        break
if c==2:
    print("Yes")
else:
    print("No")
