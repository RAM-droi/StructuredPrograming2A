length=0
width=0
area=0

length = int(input("Enter the lenght of the rectangle:" ))
width = int(input("Enter the width of the rectangle:" ))
area = length * width
if length == width:
    print("This rectangle is square" )
print(f"The area of this rectangle is: {area}")
