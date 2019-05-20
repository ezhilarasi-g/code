#ezhil
from itertools import permutations
n=input()
a=permutations(n)
for i in list(a):
    print("".join(i))
