#ezhil
a,b=map(int,input().split())
if a>b:
    c=a-b
else:
    c=b-a
if c%2==0:
    print("even")
else:
    print("odd")
