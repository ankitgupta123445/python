x=int(input("enter the x coordinate of center"))
y=int(input("enter the y coordinate of center"))
r=int(input("enter the radius of circle"))
x1=int(input("enter the x coordinate of arbitrary point"))
y1=int(input("enter the y coordinate of arbitrary point"))
z=((x-x1)**2+(y-y1)**2)**0.5
if z==0:
    print("point are lie on the center of cicle")
elif z<r:
    print("points is lie inside the circle")
elif z==r:
    print("points is lie on the circle")
else :
    print("points is lie outside the circle")
       
