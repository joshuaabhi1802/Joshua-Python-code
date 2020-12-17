import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
a=int(input())
b=0
i=0
while a>0:
    c=a%10
    b=b+c*8**i
    i=i+1
    a=a//10
print(b)