#ezhil
a=int(input())
b=input()
c=b.lower()
s=c[::-1]
l=list(str(s))
for i in l:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        l.remove(i)
        d=''.join(map(str,l))
print(d)
