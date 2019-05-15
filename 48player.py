#ezhil
a=int(input())
res=''
for i in range(1,a+1):
    if a%i==0:
        if i%2==1:
            res=res+str(i)+' '
print(res.strip())
