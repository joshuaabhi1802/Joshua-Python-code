import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
a=int(input())
x=input()
for i in range(a):
    for j in range(i+1):
        print(x,end=' ')
    print()
for i in range(a-1,0,-1):
    for j in range(i):
        print(x,end=' ')
    print()
