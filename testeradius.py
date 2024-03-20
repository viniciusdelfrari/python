# Import math library for pi (π) constant
import math

# Prompt user for radius input
radius = float(input("Enter the radius of the circle: "))

# Calculate diameter using d = 2r
diameter = 2 * radius

# Calculate circumference using c = 2πr
circumference = 2 * math.pi * radius

# Calculate area using A = 3.14 * r * r
area = 3.14 * radius * radius

# Print formatted results with two decimal places
print(f"For a circle with radius {radius:.0f}:")
print(f"\tDiameter: {diameter:.0f}")
print(f"\tCircumference: {circumference:.2f}")
print(f"\tArea: {area:.2f}")
