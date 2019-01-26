#ezhil
n=input()
l=list(n)
a=len(n)
if a%2==1:
    l[a//2]='*'
else:
    l[a//2],l[(a//2)-1]="*","*"
s="".join(l)
print(s)
  
