import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
a=int(input())
b=input()
c="*"
print(a*c+b+a*c)