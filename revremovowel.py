#ezhil
a=int(input())
b=input()
s=b[::-1]
l=list(str(s))
for i in l:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="O" or i=="I" or i=="U":
        l.remove(i)
        d=''.join(map(str,l))
print(d)
