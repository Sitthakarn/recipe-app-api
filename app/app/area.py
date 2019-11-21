from math import pi

def circle_area(radius):
    return pi*(radius**2)

radii = [2, 0, -3, 2 + 5j, True]
""", "redius"]"""
message = "Area of circles with r = {radius} is {area}."

for r in radii:
    A = circle_area(r)
    print(message.format(radius=r, area=A))
