print("Rectangle")
print("......")
l=int(input("enter length of rectangle : "))
b=int(input("enter breadth of rectangle: "))
area=lambda l,b :l*b
print("area of rectangle is ",area(l,b))
per=lambda l,b:2*(l+b)
print("perimeter of rectangle is",per(l,b))
print("square")
print("......")
a=int(input("enter length of one side of square: "))
area=lambda a:a*a
print("area of square is",area(a))
per=lambda a:4*a
print("perimeter of square is",per(a))


