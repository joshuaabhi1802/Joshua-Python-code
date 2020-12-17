import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
class Student:
    def __init__(self,name,age,have_aadhar):
        self.name = name 
        self.age = age
        self.have_aadhar= have_aadhar
    def check_vote_eligibility(self):
        if self.age>18 and self.have_aadhar=='YES':
            print('You are eligible to vote')
        elif self.age>18 and self.have_aadhar!='YES':
            print('Get you aadhar first to vote')
        else:
            print('You are not eligible to vote')
if __name__ == "__main__":
    a=int(input())
    for i in range(a):
        b=input().split()
        b[1]= int(b[1])
        s= Student(b[0],b[1],b[2])
        s.check_vote_eligibility()




