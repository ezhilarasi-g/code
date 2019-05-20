#ezhil
n=input()
a=[]
for i in n.split():
    a.append(i[::-1])
print(*a)
