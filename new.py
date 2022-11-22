def AreaOfRectangle(l,b):
    return l*b

def AreaOfCircle(r):
    return 3.14*r**2

length=eval(input("Enter length : "))
breadth=eval(input("Enter breadth : "))
print("Area of rectangle = ",AreaOfRectangle(length,breadth))

radius=eval(input("Enter radius of circle : "))
print("Area of circle = ",AreaOfCircle(radius))