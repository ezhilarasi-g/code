#ezhil
l,r=map(int,input().split())
a=l*r
for i in range(a,0,-1):
    if l%i==0 and r%i==0:
        print(i)
        break
