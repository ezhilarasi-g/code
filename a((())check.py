#ezhil
n=input()
for i in n:
    c=n.count('(')
    d=n.count(')')
if c==d:
    print("yes")
else:
    print("no")
