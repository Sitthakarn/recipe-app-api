from math import pi

def circle_area(radius):
    if type(radius) not in [int, float]:
        raise TypeError("The radius is not number")
    if radius < 0:
        raise ValueError("The radius is less than zero.")
    return pi*(radius**2)

""""
radii = [2, 0, -3, 2 + 5j, True]
message = "Area of circles with r = {radius} is {area}."

for r in radii:
    A = circle_area(r)
    print(message.format(radius=r, area=A))
"""