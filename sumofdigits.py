import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
a=int(input())
m=0
while a>0:
    m=a%10 +m
    a=a//10
print(m)

