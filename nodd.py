a,b=map(int,input().split())
x=''
for i in range(a+1,b):
	if i%2==1:
		x=x+str(i)+' '
print(x.strip())
