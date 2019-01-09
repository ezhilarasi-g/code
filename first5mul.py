#ezhil
n=int(input())
x=' '
if n>0:
	for i in range(1,6):
		num=i*n
		x=x+str(num)+' '
	print(x.strip())
