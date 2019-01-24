#ezhil
n=int(input())
l=[2,4,6,8,0]
for i in (l):
    r=n%10
    if r in l:
        print("yes")
        break
    else:
        print("no")
    
