class Student:
    def __init__(self,name,phy,chem,bio):
        self.name=name
        self.phy=phy
        self.chem=chem
        self.bio=bio
        

    def totalObtained(self):
        return self.phy+self.chem+self.bio

    def percentage(self):
        return (self.totalObtained()/3)
    
name=input('enter your name')
phy=int(input('enter physics marks'))
chem=int(input('enter chemistry marks'))
bio=int(input('enter biology marks'))    

s=Student(name,phy,chem,bio)        
print(s.totalObtained())
print(s.percentage())
