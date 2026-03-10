class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return  self.length * self.width   
    def parameter(self):
        return 2 * (self.width+self.length)
    
rad=Rectangle(5,6)  
print( rad.area())
print(rad.parameter())  