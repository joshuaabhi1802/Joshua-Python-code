import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a=input()
print(a[0:10])
print(a[4:13])
print(a[::2])
