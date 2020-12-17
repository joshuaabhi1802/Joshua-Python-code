import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
a=int(input())
if a==1:
    print("Neither prime nor composite")
    exit()   
p=1
import math
b=int(math.sqrt(a))
for i in range(2,b+1):
    if a%i==0:
        p=0
        break
if p==1:
    print("Prime Number")
else:
    print("Not a prime number")
