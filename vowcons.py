x=['a','e','i','o','u','A','E','I','O','U']
n=input()
if n.isalpha():
	if n in x:
		print("Vowel")
	else:
		print("Consonant")
else:
	print("invalid")
