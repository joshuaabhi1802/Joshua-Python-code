import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
a=int(input())
b=[]
while a>0:
    m=a%16
    b.append(m)
    a=a//16
for i in range (len(b)):
    if b[i]>9:
        d=b[i]-10
        b[i]=chr(d+65)
for i in range (len(b)):
    print(b[len(b)-i-1],end='')