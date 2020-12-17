import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a=input()
b=a[::-1]
if a==b:
    print("palindrome")
else:
    print("not a palindrome")