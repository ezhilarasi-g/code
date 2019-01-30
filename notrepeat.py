#ezhil
n=input()
d={}
a=[]
for i in n:
    c=n.count(i)
    d.update({i:c})
    a.append(c)
for x,y in d.items():
    if y==1:
        print(x)
