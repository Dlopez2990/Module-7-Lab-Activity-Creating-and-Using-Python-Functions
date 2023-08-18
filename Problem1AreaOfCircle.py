# Daniel L
# 8/18/23
# Problem 1 function to find the radius of an area of the circle. 
import math

def area_of_circle(r):
    if r < 0:
        raise ValueError("Radius cannot be negative")
    
    area = math.pi * (r ** 2)
    return area

def main():
    radius = float(input("Enter the radius of the circle: "))
    circle_area = area_of_circle(radius)
    print(f"The area of a circle with radius {radius} is {circle_area}")

if __name__ == "__main__":
    main()
