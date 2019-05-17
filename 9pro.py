#ezhil
n=int(input())
l=list(map(int,input().split()))
for i in range(0,len(l)):
	for j in range(i,len(l)-1):
	    if l[i]+l[j]==0:
	        print(l[i],l[j])
