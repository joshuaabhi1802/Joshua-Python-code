import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
a=int(input())
b=[]
while a>0:
    m=a%8
    b.append(m)
    a=a//8
for i in range (len(b)):
    print(b[len(b)-i-1],end='')
       