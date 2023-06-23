class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return self.x**2+self.y**2+self.z**2

a=int(input('enter first number'))
b=int(input('enter second number'))
c=int(input('enter third number'))

s=Point(a,b,c)
print(s.sqSum())