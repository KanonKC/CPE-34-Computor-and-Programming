class Rectangle:
    def __init__(self,l,w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w
    
    def perimeter(self):
        return (self.l + self.w)*2

    def is_square(self):
        if self.l == self.w:
            return "This rectangle is square too."
        else:
            return "This rectangle is not square."
    
l = int(input("Enter rectangle length : "))  
w = int(input("Enter rectangle width : "))  
p1 = Rectangle(l,w)
print(f'Area is {p1.area()}.')  
print(f'Perimeter is {p1.perimeter()}.')  
print(p1.is_square()) 

class Triangle:
    def __init__(self,l1,l2,l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def area(self):
        s = (self.l1+self.l2+self.l3)/2
        return ((s-self.l1)*(s-self.l2)*(s-self.l3)*s)**(1/2)

    def perimeter(self):
        return self.l1+self.l2+self.l3
    def is_right_triangle(self):
        top = max(self.l1,self.l2,self.l3)
        # print(top)
        side = [self.l1,self.l2,self.l3]
        side.remove(top)
        # print(side)
        if side[0]**2 + side[1]**2 == top**2:
            return "This triangle is right triangle too."
        else:
            return "This triangle is not right triangle."

l1 = int(input("Enter triangle first side length : "))  
l2 = int(input("Enter triangle second side length : "))  
l3 = int(input("Enter triangle third side length : "))  
p2 = Triangle(l1,l2,l3)
print(f'Area is {p2.area()}.')  
print(f'Perimeter is {p2.perimeter()}.')  
print(p2.is_right_triangle()) 

class Circle:
    def __init__(self,r):
        self.r = r

    def area(self):
        return 3.14*(self.r**2)
    
    def perimeter(self):
        return 2*3.14*self.r

    

r = int(input("Enter circle radius : "))  
p3 = Circle(r)
print(f'Area is {p3.area()}.')  
print(f'Perimeter is {p3.perimeter()}.')