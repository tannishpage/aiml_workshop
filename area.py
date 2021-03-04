def area_triangle(base, height):
    area = 0.5*base*height
    return area

def area_square(side_length):
    area = side_length * side_length
    return area

def area_rectangle(width, length):
    area = width * length
    return area


print("Area of triangle with base length 1m and height 2m is:", area_triangle(1, 2), "m^2")
print("Area of square with side length of 2m is:", area_square(2), "m^2")
print("Area of rectangle with width of 2m and length of 3m is:", area_rectangle(2, 3), "m^2")
