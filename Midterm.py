import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    result = math.pi * radius**2
    return round(result, 2)
print(area_of_circle(5))


# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    return ""

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    result = ""

    for i in range(n):
        for j in range(n):
            if i == n - 1 or j == 0 or j == i:
                result += "*"
            else:
                result += " "
        result += "\n"

    return result.rstrip()
print(hollow_right_triangle(3))
print(hollow_right_triangle(4))
print(hollow_right_triangle(5))


# Q3: Inverted Pyramid
def inverted_pyramid(n):
    return ""

# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()
