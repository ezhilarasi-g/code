#ezhil
n=int(input())
k=input()
a=""
c=""
for i in range(len(k)):
    if k[i]=='1':
        a=a+k[i]+' '
    else:
        c=c+a
        a=""
print(c.strip())
