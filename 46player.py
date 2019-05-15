#ezhil
import math
n=int(input())
r=n*(math.pi)/180
if r>0 and r<1:
    print(round(math.sin(r),2))
else:
    print(round(math.sin(r)))
