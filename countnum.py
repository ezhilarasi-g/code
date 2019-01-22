#ezhil
s=input()
c=0
for i in range(len(s)):
	if s[i].isnumeric():
		c=c+1
print(c)
