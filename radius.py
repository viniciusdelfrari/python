# Prompt user for radius input
r = float(input("Enter the radius of a circle: "))

# Calculate diameter using d = 2*r
d = 2 * r

# Calculate circumference using c = 2*3.14*r
c = 2 * 3.14 * r

# Calculate area using a = 3.14 * r * r (I used ":.0f" and ":.2f" to determine the number of numbers after the dot.)
a = 3.14 * r * r
print(f"A circle with a radius of {r:.0f} units will have a diameter of {d:.0f} units, a circumference of {c:.2f} units and an area of {a} square units.")