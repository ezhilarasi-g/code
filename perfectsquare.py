#ezhil
import math
a,b=map(int,input().split())
c=a*b
sq=math.sqrt(c)
insq=int(sq)
print(insq)
if insq==sq:
    print("yes")
else:
    print("no")
