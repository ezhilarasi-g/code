#ezhil
n=input()
for i in range(1,len(n)):
    if n[:i]==n[i+1:]:
        f=1
        break
    else:
        f=0
if f==1:
    print("YES")
else:
    print("NO")
