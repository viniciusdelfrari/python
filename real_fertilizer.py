import math

# Input dimensions of the sections
front_length = float(input("What is the length of the front section? "))
front_width = float(input("What is the width of the front section? "))
rear_length = float(input("What is the length of the rear section? "))
rear_width = float(input("What is the width of the rear section? "))
left_length = float(input("What is the length of the left section? "))
left_width = float(input("What is the width of the left section? "))
right_length = float(input("What is the length of the right section? "))
right_width = float(input("What is the width of the right section? "))

# Fixed cost per bag of fertilizer
cost_per_bag = 27  # Fixed cost per bag

# Fixed labor rate per hour
labor_rate_per_hour = 20  # Fixed labor rate per hour

# Calculate total area
front_area = front_length * front_width
rear_area = rear_length * rear_width
left_area = left_length * left_width
right_area = right_length * right_width
total_area = front_area + rear_area + left_area + right_area

# Calculate bags of fertilizer needed
bags_of_fertilizer = total_area / 2000
bags_of_fertilizer = math.ceil(bags_of_fertilizer)

# Calculate total cost of fertilizer
fertilizer_cost = bags_of_fertilizer * cost_per_bag

# Calculate total labor hours and labor cost
labor_hours = total_area / 2500
labor_hours_rounded_up = math.ceil(labor_hours)
labor_cost = labor_hours_rounded_up * labor_rate_per_hour

# Calculate total cost to the company
total_cost = fertilizer_cost + labor_cost

# Calculate pounds of nitrogen and potassium
pounds_of_nitrogen = bags_of_fertilizer * 0.5
pounds_of_potassium = bags_of_fertilizer * 0.125

# Output the results
print(f"Your application has a total area of {total_area} sq. feet. That will require {bags_of_fertilizer} bags of fertilizer. The cost of the fertilizer will be ${fertilizer_cost:.2f}.")
print(f"Our technicians will require {labor_hours_rounded_up} hours to finish the job and the labor cost will be ${labor_cost:.2f}.")
print(f"The total cost to the company will be ${total_cost:.2f}. The application will result in {pounds_of_nitrogen:.0f} pounds of nitrogen and {pounds_of_potassium:.3f} pounds of potassium being added to the soil.")
