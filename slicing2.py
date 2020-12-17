import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a=input()
b=input()
c=a[1:]+b[:7]
print (c)