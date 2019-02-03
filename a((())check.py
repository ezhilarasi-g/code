#ezhil
n=input()
for i in n:
    c=n.count('(')
    d=n.count(')')
if c==d:
    print("Yes")
else:
    print("No")
