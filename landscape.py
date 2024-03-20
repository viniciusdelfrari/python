import math

# Input dimensionss
L1 = float(input("What is the length of the front section? "))
W1 = float(input("What is the width of the front section? "))
L2 = float(input("What is the length of the rear section? "))
W2 = float(input("What is the width of the rear section? "))
L3 = float(input("What is the length of the left section? "))
W3 = float(input("What is the width of the left section? "))
L4 = float(input("What is the length of the right section? "))
W4 = float(input("What is the width of the right section? "))

# Calculate total area
front_area = L1 * W1
rear_area = L2 * W2
left_area = L3 * W3
right_area = L4 * W4
total_area = front_area + rear_area + left_area + right_area

# Calculate bags of fertilizer needed
bags_of_fertilizer = total_area / 2000
unrounded_bags = total_area / 2000
bags_of_fertilizer = math.ceil(bags_of_fertilizer)

cost_per_bag = 27  # cost per bag

# Calculate total cost of fertilizer
fertilizer_cost = bags_of_fertilizer * cost_per_bag 

labor_rate_per_hour = 20  # labor rate per hour

# Calculate total labor hours and labor cost
labor_hours = total_area / 2500
labor_hours = math.ceil(labor_hours)
labor_cost = labor_hours * labor_rate_per_hour

# Calculate total cost to the company
total_cost = fertilizer_cost + labor_cost

# Calculate pounds of nitrogen and potassium
pounds_of_nitrogen = unrounded_bags * 1
pounds_of_potassium = unrounded_bags * 0.125

# Print results
print(f"Your application has a total area of {total_area} sq. feet. That will require {bags_of_fertilizer} bags of fertilizer. The cost of the fertilizer will be ${fertilizer_cost:.2f}.")
print(f"Our technicians will require {labor_hours} hours to finish the job and the labor cost will be ${labor_cost:.2f}.")
print(f"The total cost to the company will be ${total_cost:.2f}. The application will result in {pounds_of_nitrogen:.3f} pounds of nitrogen and {pounds_of_potassium:.3f} pounds of potassium being added to the soil.")
