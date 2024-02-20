import math

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2 * math.pi * self.radius**2 + 2 * math.pi * self.radius * self.height

    def volume(self):
        return math.pi * self.radius**2 * self.height


# # Here height = 10 and radius = 8

# Creating Object 
c = Cylinder(10,8)
sa = round(c.surface_area(),4)
print(f"The surface area of Cylinder is {sa}")

vol = round(c.volume(),4)
print(f"The volume of Cylinder is {vol}")



# Using function annotations
def cylinder_surface_area(radius: float, height: float) -> float:
    return 2 * math.pi * radius**2 + 2 * math.pi * radius * height

def cylinder_volume(radius: float, height: float) -> float:
    return math.pi * radius**2 * height

sa = round(cylinder_surface_area(4,9),4)
vol = round(cylinder_volume(4,9),4)

print(f"The surface area of Cylinder is {sa}")
print(f"The volume of Cylinder is {vol}")

