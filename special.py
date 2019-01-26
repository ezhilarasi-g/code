#ezhil
n=input()
c=0
for i in range(len(n)):
	if n[i].isalpha():
		pass
	elif n[i].isnumeric():
		pass
	else:
		c=c+1
print(c)
