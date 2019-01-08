#ezhil
n=int(input())
rev=0
b=n
while n>0:
	r=n%10
	rev=rev*10+r
	n=n//10
if rev==b:
	print("yes")
else:
	print("no")
		
		
	
