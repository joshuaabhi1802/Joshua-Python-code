import math
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
m=int(input())
n=int(input())
for a in range(m,n+1):
    p=1
    import math
    b=int(math.sqrt(a))
    for i in range(2,b+1):
        if a%i==0:
            p=0
            break
    if p==1:
        print(a)