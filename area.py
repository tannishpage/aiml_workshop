import mathn

def area_triangle(base, height):
    area = 0.5*base*height
    return area

def area_square(side_length):
    area = side_length ** 2
    return area

def area_rectangle(width, length):
    area = width * length
    return area

def area_circle(radius):
    area = math.pi * (radius ** 2)


print("Area of triangle with base length 1m and height 2m is:", area_triangle(1, 2), "m^2")
print("Area of square with side length of 2m is:", area_square(2), "m^2")
print("Area of rectangle with width of 2m and length of 3m is:", area_rectangle(2, 3), "m^2")
print("Area of circle with radius of 2m is:", area_circle(2), "m^2")
