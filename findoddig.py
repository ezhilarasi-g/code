#ezhil
n=input()
res=''
for i in n:
    i=int(i)
    if i%2!=0:
        res=res+str(i)+' '
print(res.strip())
        
