import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
a=input().split()
a=[int(i) for i in a]
m=a[0]
for i in range(len(a)):
    if m>a[i]:
        m=a[i]
print("Smallest Number:",m)

