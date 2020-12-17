import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
a=input()
a = list(a)
for i in range(len(a)):
    if ord(a[i]) > 57:
        b = ord(a[i]) - 65 + 10
        a[i] = b
a = [int(i) for i in a]
deci_num=0
j=0
for i in range (len(a)-1,-1,-1):
    deci_num+=a[i]*16**j
    j+=1
print(deci_num)

