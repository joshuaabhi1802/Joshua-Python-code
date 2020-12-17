import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
a=input().split()
product=1
for i in range(len(a)):
    a[i]=int(a[i])
    product=product*a[i]
print("PRODUCT:",product)
