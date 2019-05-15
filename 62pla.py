#ezhil
n=int(input())
for i in range(0,n+1):
    x=n%i
    if x%2!=0:
        print(i)
        break
