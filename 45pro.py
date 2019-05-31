#ezhil
n=input()
c=1
if n==n[::-1]:
    print("yes")
else:
    x=n.strip("0")
    #print(x)
    if x==x[::-1]:
        print("yes")
    else:
        print("no")
