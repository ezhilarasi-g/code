#ezhil
n=input()
s=''
for i in n:
    if i.isupper():
        s=s+i.lower()
    else:
        s=s+i.upper()
print(s)
        
