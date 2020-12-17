class mensuration:
    def __init__(self,radius):
        self.radius=radius
        self.pi= 22/7
    def area_circle(self):
        area = self.pi*self.radius**2
        return area
    def perimeter_circle(self):
        perimeter = 2*self.pi*self.radius
        return perimeter
    def volume_sphere(self):
        volume= 4/3*self.pi*self.radius**3
        return volume
if __name__ == "__main__":
    print("Enter the radius")
    a=int(input())
    print("Please select the options given below-\n1.Area of circle\n2.Perimeter of circle\n3.Volume of sphere")
    b=int(input())
    s= mensuration(a)
    if b==1:
        print('Area is:',s.area_circle())
    if b==2:
        print('Perimeter is:',s.perimeter_circle())
    if b==3:
        print('Volume is:',s.volume_sphere())
    


