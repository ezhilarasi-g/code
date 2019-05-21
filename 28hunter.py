#ezhil
s=input()
a=list(s)
b=set(a)
c=sorted(b)
res=''
for i in c:
    res=res+i+''
print(res.strip())
