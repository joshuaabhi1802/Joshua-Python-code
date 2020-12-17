import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
a=list(input())
print(a)
for i in range(len(a)):
    a[i]=int(a[i])
    sum=sum+a[i]
print("SUM:",sum)

