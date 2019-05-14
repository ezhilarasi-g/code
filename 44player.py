#ezhil
a,b=map(str,input().split())
c=int(b)
d=len(a)
for i in range(0,c+1):
    s=a[-i:]+a[:d-i]
print(s)
