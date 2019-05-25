#ezhil
n=int(input())
l=list(map(int,input().split()))
for i in range(0,len(l)):
    if n==1:
        print(l[i])
        break
    elif l[i]==l[i+1]:
        print(l[i])
        break
    else:
        print("0")
        break
